##############################################################
Type deduction for objects using the auto keyword
##############################################################

Introduction
***************

Because C++ is a strongly-typed language, developers are required to provide an explicit type for all objects.

However, some variables are initialized with literals (which have a type). So, in cases where a variable and its initializer have the same type, it is being provided the same type information twice.

Type deduction for initialized variables
******************************************

**Type deduction** (also sometimes called **type inference**) is a feature that allows the compiler to deduce the type of an object from the object's initializer. To use type deduction, the ``auto`` keyword is used in place of the variable's type:

.. code-block:: cpp

    int main()
    {
        auto d{ 5.0 }; // 5.0 is a double literal, so d will be type double
        auto i{ 1 + 2 }; // 1 + 2 evaluates to an int, so i will be type int
        auto x { i }; // i is an int, so x will be type int too

        return 0;
    }

Because function calls are valid expressions, type deduction  can also be used when the initializer is a function call:

.. code-block:: cpp

    int add(int x, int y)
    {
        return x + y;
    }

    int main()
    {
        auto sum { add(5, 6) }; // add() returns an int, so sum's type will be deduced to int
        return 0;
    }

Type deduction will not work for objects that do not have initializers or empty initializers.

Type deduction drops const qualifiers
***************************************

In most cases, type deduction will drop the const qualifier from deduced types. For example:

.. code-block:: cpp

    int main()
    {
        const int x { 5 }; // x has type const int
        auto y { x };      // y will be type int (const is dropped)
    }

If the deduced type is wanted to be const, the ``const`` keyword must be also provided. To do so, simply use the ``const`` keyword in conjunction with the ``auto`` keyword:

.. code-block:: cpp

    int main()
    {
        const int x { 5 };  // x has type const int
        auto y { x };       // y will be type int (const is dropped)

        const auto z { x }; // z will be type const int (const is reapplied)
    }

Type deduction for string literals
************************************

For historical reasons, string literals in C++ have a strange type. Therefore, the following probably won’t work as expected:

.. code-block:: cpp

    auto s { "Hello, world" }; // s will be type const char*, not std::string

To use type deduction from a string literal and be std::string or std::string_view, the use of the ``s`` or ``sv`` literal suffixes is needed.

Type deduction benefits and downsides
***************************************

Type deduction is not only convenient, but also has a number of other benefits.

#. type deduction only works on variables that have initializers, so type deduction can help avoid unintentionally uninitialized variables:

.. code-block:: cpp

    int x; // oops, we forgot to initialize x, but the compiler may not complain
    auto y; // the compiler will error out because it can't deduce a type for yç

#. it is guaranteed that there will be no unintended performance-impacting conversions:

.. code-block:: cpp

    double x { 5 }; // bad: implicitly converts 5 from an int to a double
    auto y { 5 }; // good: y is an int (hopefully that's what you wanted) and no conversion takes place

Type deduction also has a few downsides.

#. type deduction obscures an object's type information in the code. Although a good IDE should be able to show you the deduced type (e.g. when hovering a variable), it's still a bit easier to make type-based mistakes when using type deduction.
#. if the type of an initializer changes, the type of a variable using type deduction will also change, perhaps unexpectedly.
