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

Here is an example of a piece of code using namespaces:

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

Qualified and unqualified names
********************************

A name can be either qualified or unqualified.

A **qualified name** is a name that includes an associated scope. Most often, names are qualified with a namespace using the scope resolution operator (``::``). For example:

.. code-block:: cpp
    :linenos:

    std::cout // identifier cout is qualified by namespace std
    ::foo // identifier foo is qualified by the global namespace

An **unqualified name** is a name that does not include a scoping qualifier.

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

Another way is to use ``using declaration`` statement.

A using declaration allows us to use an unqualified name (with no scope) as an alias for a qualified name.

.. code-block:: cpp
    :linenos:

    int main()
    {
        using std::cout; // this using declaration tells the compiler that cout should resolve to std::cout
        cout << "Hello world!"; // so no std:: prefix is needed here!

        return 0;
    } // the using declaration expires here

Note that a separate ``using declaration``is required for each name (e.g. one for ``std::cout``, one for ``std::cin``, etc…). Although this method is less explicit than using the std:: prefix, it's generally considered safe and acceptable (when used inside a function).

If a ``using declaration`` or ``using directive`` is used within a block, the names are applicable to just that block (it follows normal block scoping rules). This is a good thing, as it reduces the chances for naming collisions to occur to just within that block.

If a ``using declaration`` or ``using directive`` is used in the global namespace, the names are applicable to the entire rest of the file (they have file scope).

Once a ``using statement`` has been declared, there's no way to cancel or replace it with a different using statement within the scope in which it was declared.

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

The way to create an alias is by means of the ``namespace`` keyword and the use of the same nomenclature that is used to assign a variable.

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

Unnamed (anonymous) namespaces
*******************************

An **unnamed namespace** (also called an **anonymous namespace**) is a namespace that is defined without a name

.. code-block:: cpp
    :linenos:

    namespace // unnamed namespace
    {
        void doSomething() // can only be accessed in this file
        {
            std::cout << "v1\n";
        }
    }

    int main()
    {
        doSomething(); // we can call doSomething() without a namespace prefix

        return 0;
    }

All content declared in an ``unnamed namespace`` is treated as if it is part of the parent namespace.

This might make ``unnamed namespaces`` seem useless. But the other effect of ``unnamed namespaces`` is that all identifiers inside an ``unnamed namespace`` are treated as if they had ``internal linkage``, which means that the content of an ``unnamed namespace`` can't be seen outside of the file in which the ``unnamed namespace`` is defined.

For functions, this is effectively the same as defining all functions in the ``unnamed namespace`` as ``static functions``.

``Unnamed namespaces`` are typically used when you have a lot of content that you want to ensure stays local to a given file, as it's easier to cluster such content in an ``unnamed namespace`` than individually mark all declarations as ``static``.

``Unnamed namespaces`` will also keep ``user-defined types`` local to the file, something for which there is no alternative equivalent mechanism to do.

Inline namespaces
*******************

An **inline namespace** is a namespace that is typically used to version content. Much like an ``unnamed namespace``, anything declared inside an ``inline namespace`` is considered part of the parent namespace. However, ``inline namespaces`` don't give everything ``internal linkage``.

To define an inline namespace, the ``inline`` keyword is used:

.. code-block:: cpp
    :linenos:

    inline namespace v1 // declare an inline namespace named v1
    {
        void doSomething()
        {
            std::cout << "v1\n";
        }
    }

    namespace v2 // declare a normal namespace named v2
    {
        void doSomething()
        {
            std::cout << "v2\n";
        }
    }

    int main()
    {
        v1::doSomething(); // calls the v1 version of doSomething()
        v2::doSomething(); // calls the v2 version of doSomething()

        doSomething(); // calls the inline version of doSomething() (which is v1)

        return 0;
    }

In the above example, callers to ``doSomething`` will get the v1 (the inline version) of ``doSomething``. Callers who want to use the newer version can explicitly call ``v2::dosomething()``.

This tool preserves the function of existing programs while allowing newer programs to take advantage of newer/better variations.
