#######################
Overloading functions
#######################

Consider the following function:

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    {
        return x + y;
    }

This trivial function adds two integers and returns an integer result. However, what if it is desired to have a function that can add two floating point numbers? This ``add()`` function is not suitable, as any floating point parameters would be converted to integers, causing the floating point arguments to lose their fractional values.

One way to work around this issue is to define multiple functions with slightly different names:

.. code-block:: cpp
    :linenos:

    int addInteger(int x, int y)
    {
        return x + y;
    }

    double addDouble(double x, double y)
    {
        return x + y;
    }

However, for best effect, this requires that you define a consistent function naming standard for similar functions that have parameters of different types, remember the names of these functions, and actually call the correct one.

And then what happens when it is wanted to have a similar function that uses 3 integers instead of 2? Managing unique names for each function quickly becomes burdensome.

Introduction to function overloading
*************************************

Fortunately, C++ has an elegant solution to handle such cases. Function overloading allows us to create multiple functions with the same name, so long as each identically named function has different parameter types (or the functions can be otherwise differentiated). Each function sharing a name (in the same scope) is called an overloaded function (sometimes called an overload for short).

To overload the ``add()`` function, it is simply required to declare another ``add()`` function that takes parameters of ``double`` type:

.. code-block:: cpp
    :linenos:

    double add(double x, double y)
    {
        return x + y;
    }

Now there are two versions of ``add()`` in the same scope:

.. code-block:: cpp
    :linenos:

    int add(int x, int y) // integer version
    {
        return x + y;
    }

    double add(double x, double y) // floating point version
    {
        return x + y;
    }

    int main()
    {
        return 0;
    }

The above program will compile. Although it might be expected these functions to result in a naming conflict, that is not the case here. Because the parameter types of these functions differ, the compiler is able to differentiate these functions, and will treat them as separate functions that just happen to share a name.

Functions can be overloaded so long as each overloaded function can be differentiated by the compiler. If an overloaded function can not be differentiated, a compile error will result.

Introduction to overload resolution
************************************

Additionally, when a function call is made to a function that has been overloaded, the compiler will try to match the function call to the appropriate overload based on the arguments used in the function call. This is called **overload resolution**.

Here's a simple example demonstrating this:

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    {
        return x + y;
    }

    double add(double x, double y)
    {
        return x + y;
    }

    int main()
    {
        std::cout << add(1, 2); // calls add(int, int)
        std::cout << '\n';
        std::cout << add(1.2, 3.4); // calls add(double, double)

        return 0;
    }

Function overload differentiation
***********************************

How overloaded functions are differentiated
--------------------------------------------

+-----------------------+---------------------------+-----------------------------------------------------------------------------------------------+
| Function property     | Used for differentiation  | Notes                                                                                         |
+=======================+===========================+===============================================================================================+
| Number of parameters  | Yes                       |                                                                                               |
+-----------------------+---------------------------+-----------------------------------------------------------------------------------------------+
| Type of parameters    | Yes                       | Excludes typedefs, type aliases, and const qualifier on value parameters. Includes ellipses.  |
+-----------------------+---------------------------+-----------------------------------------------------------------------------------------------+
| Return type           | No                        |                                                                                               |
+-----------------------+---------------------------+-----------------------------------------------------------------------------------------------+

Note that a function's return type is not used to differentiate overloaded functions.

For member functions, additional function-level qualifiers are also considered:

+---------------------------+-----------------------+
| Function-level qualifier  | Used for overloading  |
+===========================+=======================+
| const or volatile         | Yes                   |
+---------------------------+-----------------------+
| Ref-qualifiers            | Yes                   |
+---------------------------+-----------------------+

As an example, a const member function can be differentiated from an otherwise identical non-const member function (even if they share the same set of parameters).

Overloading based on number of parameters
--------------------------------------------

An overloaded function is differentiated so long as each overloaded function has a different number of parameters. 

For example:

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    {
        return x + y;
    }

    int add(int x, int y, int z)
    {
        return x + y + z;
    }

The compiler can easily tell that a function call with two integer parameters should go to ``add(int, int)`` and a function call with three integer parameters should go to ``add(int, int, int)``.

Overloading based on type of parameters
--------------------------------------------

A function can also be differentiated so long as each overloaded function's list of parameter types is distinct. 

For example, all of the following overloads are differentiated:

.. code-block:: cpp
    :linenos:

    int add(int x, int y); // integer version
    double add(double x, double y); // floating point version
    double add(int x, double y); // mixed version
    double add(double x, int y); // mixed version

Because type aliases (or typedefs) are not distinct types, overloaded functions using type aliases are not distinct from overloads using the aliased type. 

For example, all of the following overloads are not differentiated (and will result in a compile error):

.. code-block:: cpp
    :linenos:

    typedef int height_t; // typedef
    using age_t = int; // type alias

    void print(int value);
    void print(age_t value); // not differentiated from print(int)
    void print(height_t value); // not differentiated from print(int)

For parameters passed by value, the const qualifier is also not considered. Therefore, the following functions are not considered to be differentiated:

.. code-block:: cpp
    :linenos:

    void print(int);
    void print(const int); // not differentiated from print(int)

Ellipsis parameters are considered to be a unique type of parameter:

.. code-block:: cpp
    :linenos:

    void foo(int x, int y);
    void foo(int x, ...); // differentiated from foo(int, int)

The return type of a function is not considered for differentiation
---------------------------------------------------------------------

A function's return type is not considered when differentiating overloaded functions.

So, the following example is generating a compiler error:

.. code-block:: cpp
    :linenos:

    int getRandomValue();
    double getRandomValue();

.. note::

    This was an intentional choice, as it ensures the behavior of a function call can be determined independently of the rest of the expression, making understanding complex expressions much simpler. Put another way, which version of a function will be called can be always determined based solely on the arguments in the function call. If return values were used for differentiation, then there wouldn't be an easy syntactic way to tell which overload of a function was being called. It'd also be needed to understand how the return value was being used, which requires a lot more analysis.

The best way to address this is to give the functions different names:

.. code-block:: cpp
    :linenos:

    int getRandomInt();
    double getRandomDouble();

Type signature
---------------

A function's **type signature** (generally called a **signature**) is defined as the parts of the function header that are used for differentiation of the function. In C++, this includes the function name, number of parameter, parameter type, and function-level qualifiers. It notably does *not* include the return type.

Name mangling
--------------

When the compiler compiles a function, it performs **name mangling**, which means the compiled name of the function is altered ("mangled") based on various criteria, such as the number and type of parameters, so that the linker has unique names to work with.

For example, some function with prototype ``int fcn()`` might compile to name ``__fcn_v``, whereas ``int fcn(int)`` might compile to name ``__fcn_i``. So while in the source code, two overloaded functions share a name, in compiled code, the names are actually unique.

There is no standardization on how names should be mangled, so different compilers will produce different mangled names.

Overload resolution
*********************

With non-overloaded functions (functions with unique names), there is only one function that can potentially match a function call. That function either matches (or can be made to match after type conversions are applied), or it doesn't (and a compile error results). With overloaded functions, there can be many functions that can potentially match a function call. Since a function call can only resolve to one of them, the compiler has to determine which overloaded function is the best match. The process of matching function calls to a specific overloaded function is called overload resolution.

In simple cases where the type of the function arguments and type of the function parameters match exactly, this is (usually) straightforward:

.. code-block:: cpp
    :linenos:

    void print(int x)
    {
        std::cout << x << '\n';
    }

    void print(double d)
    {
        std::cout << d << '\n';
    }

    int main()
    {
        print(5); // 5 is an int, so this matches print(int)
        print(6.7); // 6.7 is a double, so this matches print(double)

        return 0;
    }

But what happens in cases where the argument types in the function call don’t exactly match the parameter types in any of the overloaded functions? For example:

.. code-block:: cpp
    :linenos:

    void print(int x)
    {
        std::cout << x << '\n';
    }

    void print(double d)
    {
        std::cout << d << '\n';
    }

    int main()
    {
        print('a'); // char does not match int or double
        print(5L); // long does not match int or double

        return 0;
    }

Just because there is no exact match here doesn't mean a match can't be found. After all, a ``char`` or ``long`` can be implicitly type converted to an ``int`` or a ``double.`` But which is the best conversion to make in each case?

Resolving overloaded function calls
------------------------------------

When a function call is made to an overloaded function, the compiler steps through a sequence of rules to determine which (if any) of the overloaded functions is the best match.

At each step, the compiler applies a bunch of different type conversions to the argument(s) in the function call. For each conversion applied, the compiler checks if any of the overloaded functions are now a match. After all the different type conversions have been applied and checked for matches, the step is done. The result will be one of three possible outcomes:

* No matching functions were found. The compiler moves to the next step in the sequence.
* A single matching function was found. This function is considered to be the best match. The matching process is now complete, and subsequent steps are not executed.
* More than one matching function was found. The compiler will issue an ambiguous match compile error. We'll discuss this case further in a bit.

If the compiler reaches the end of the entire sequence without finding a match, it will generate a compile error that no matching overloaded function could be found for the function call.

The argument matching sequence
--------------------------------


Ambiguous matches
------------------



Resolving ambiguous matches
----------------------------



Matching for functions with multiple arguments
-----------------------------------------------

