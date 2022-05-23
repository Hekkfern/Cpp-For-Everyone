################################################
Namespaces and the scope resolution operator
################################################

Introduction
*************

C++ requires that all identifiers be non-ambiguous. If two identical identifiers are introduced into the same program in a way that the compiler or linker can't tell them apart, the compiler or linker will produce an error. This error is generally referred to as a **naming collision** (or **naming conflict**).

As programs get larger and use more identifiers, the odds of a naming collision being introduced increases significantly. The good news is that C++ provides plenty of mechanisms for avoiding naming collisions.

What is a namespace?
*********************

A **namespace** is a region that allows you to declare names inside of it for the purpose of disambiguation. The namespace provides a scope region (called **namespace scope**) to the names declared inside of it, which simply means that any name declared inside the namespace won't be mistaken for identical names in other scopes.

Within a namespace, all names must be unique, otherwise a naming collision will result.

Namespaces are often used to group related identifiers in a large project to help ensure they don't inadvertently collide with other identifiers.

The global namespace
*********************

In C++, any name that is not defined inside a class, function, or a namespace is considered to be part of an implicitly defined namespace called the **global namespace** (sometimes also called **the global scope**).

Only declarations and definition statements can appear in the global namespace. This means variables can be defined in the global namespace, though this should generally be avoided. This also means that other types of statements (such as expression statements) cannot be placed in the global namespace (initializers for global variables being an exception).

.. code-block:: cpp
    :linenos:

    // All of the following statements are part of the global namespace
    void foo();    // okay: function forward declaration in the global namespace
    int x;         // compiles but strongly discouraged: uninitialized variable definition in the global namespace
    int y { 5 };   // compiles but discouraged: variable definition with initializer in the global namespace
    x = 5;         // compile error: executable statements not allowed in the global namespace

    int main()     // okay: function definition in the global namespace
    {
        return 0;
    }

    void goo();    // okay: another function forward declaration in the global namespace

Defining custom namespaces
*****************************

C++ allows developers to define their own namespaces via the ``namespace`` keyword. Namespaces that are created this way are called **user-defined namespaces**. 

Namespaces provided by C++ (such as the ``global namespace``) or by libraries (such as ``namespace std``) are not considered user-defined namespaces.

Namespace identifiers are typically non-capitalized.

here is an example of a piece of code using namespaces:

.. code-block:: cpp
    :linenos:

    namespace foo // define a namespace named foo
    {
        // This doSomething() belongs to namespace foo
        int doSomething(int x, int y)
        {
            return x + y;
        }
    }

It's legal to declare namespace blocks in multiple locations (either across multiple files, or multiple places within the same file). All declarations within the namespace are considered part of the namespace.

When the code is separated into multiple files, it is needed to use a namespace in the header and source file.

The scope resolution operator
******************************

The best way to tell the compiler to look in a particular namespace for an identifier is to use the **scope resolution operator** (``::``). The scope resolution operator tells the compiler that the identifier specified by the right-hand operand should be looked for in the scope of the left-hand operand.

Here is an example of using the scope resolution operator:

.. code-block:: cpp
    :linenos:

    namespace foo // define a namespace named foo
    {
        // This doSomething() belongs to namespace foo
        int doSomething(int x, int y)
        {
            return x + y;
        }
    }

    namespace goo // define a namespace named goo
    {
        // This doSomething() belongs to namespace goo
        int doSomething(int x, int y)
        {
            return x - y;
        }
    }

    int main()
    {
        std::cout << foo::doSomething(4, 3) << '\n'; // use the doSomething() that exists in namespace foo
        return 0;
    }

The scope resolution operator can also be used in front of an identifier without providing a namespace name (e.g. ``::doSomething``). In such a case, the identifier (e.g. ``doSomething``) is looked for in the global namespace.

If an identifier inside a namespace is used and no scope resolution is provided, the compiler will first try to find a matching declaration in that same namespace. If no matching identifier is found, the compiler will then check each containing namespace in sequence to see if a match is found, with the global namespace being checked last.

The using directive
********************

Another way to access identifiers inside a namespace is to use a *using directive* statement. 

A **using directive** allows us to access the names in a namespace without using a namespace prefix.

.. code-block:: cpp
    :linenos:

    using namespace std; // this is a using directive that allows us to access names in the std namespace with no namespace prefix

    int main()
    {
        cout << "Hello world!";
        return 0;
    }

So in the above example, when the compiler goes to determine what identifier ``cout`` is, it will match with ``std::cout``, which, because of the using directive, is accessible as just ``cout``.


Nested namespaces
******************

Namespaces can be nested inside other namespaces. 

For example:

.. code-block:: cpp
    :linenos:

    namespace foo
    {
        namespace goo // goo is a namespace inside the foo namespace
        {
            int add(int x, int y)
            {
                return x + y;
            }
        }
    }

    int main()
    {
        std::cout << foo::goo::add(1, 2) << '\n';
        return 0;
    }

Since C++17, nested namespaces can also be declared this way:

.. code-block:: cpp
    :linenos:

    namespace foo::goo // goo is a namespace inside the foo namespace (C++17 style)
    {
    int add(int x, int y)
    {
        return x + y;
    }
    }

    int main()
    {
        std::cout << foo::goo::add(1, 2) << '\n';
        return 0;
    }


Namespace aliases
******************

Because typing the fully qualified name of a variable or function inside a nested namespace can be painful, C++ allows creating **namespace aliases**, which allow shortening temporarily a long sequence of namespaces into something shorter.

For example:

.. code-block:: cpp
    :linenos:

    namespace foo::goo
    {
        int add(int x, int y)
        {
            return x + y;
        }
    }

    int main()
    {
        namespace active = foo::goo; // active now refers to foo::goo

        std::cout << active::add(1, 2) << '\n'; // This is really foo::goo::add()

        return 0;
    } // The active alias ends here

