#############################
Type deduction for functions
#############################

When a function is compiled, the compiler will determine the type of the returned expression, then ensure that type of the return value matches the declared return type of the function (or that the return value type can be converted to the declared return type).

Since the compiler already has to deduce the return type from the return statement, in C++14, the ``auto`` keyword was extended to do function return type deduction. This works by using the ``auto`` keyword in place of the function's return type.

For example:

.. code-block:: cpp
    :linenos:

    auto add(int x, int y)
    {
        return x + y;
    }

When using an ``auto`` return type, all return values must be of the same type, otherwise an error will result. For example:

.. code-block:: cpp
    :linenos:

    auto someFcn(bool b)
    {
        if (b)
            return 5; // return type int
        else
            return 6.7; // return type double
    }

In the above function, the two return statements return values of different types, so the compiler will give an error.

A major downside of functions that use an ``auto`` return type is that such functions must be fully defined before they can be used (a forward declaration is not sufficient). For example:

.. code-block:: cpp
    :linenos:

    auto foo();

    int main()
    {
        std::cout << foo() << '\n'; // the compiler has only seen a forward declaration at this point
        return 0;
    }

    auto foo()
    {
        return 5;
    }

This makes sense: a forward declaration does not have enough information for the compiler to deduce the function's return type. This means normal functions that return ``auto`` are typically only callable from within the file in which they are defined.

Unlike type deduction for objects, there isn't as much consensus on best practices for function return type deduction. When using type deduction with objects, the initializer is always present as part of the same statement, so it's usually not overly burdensome to determine what type will be deduced. With functions, when looking at a function's prototype, there is no context to help indicate what type the function returns. A good programming IDE should make clear what the deduced type of the function is, but in absence of having that available, a user would actually have to dig into the function body itself to determine what type the function returned. The odds of mistakes being made are higher. And the inability for such functions to be forward declared limits their usefulness in multi-file programs.

Trailing return type syntax
****************************

The ``auto`` keyword can also be used to declare functions using a **trailing return syntax**, where the return type is specified after the rest of the function prototype.

Consider the following function:

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    {
        return (x + y);
    }

Using the trailing return syntax, this could be equivalently written as:

.. code-block:: cpp
    :linenos:

    auto add(int x, int y) -> int
    {
        return (x + y);
    }

In this case, ``auto`` does not perform type deduction. It is just part of the syntax to use a trailing return type.

Why would anybody want to use this? One nice thing is that it makes all of the function names line up:

.. code-block:: cpp
    :linenos:

    auto add(int x, int y) -> int;
    auto divide(double x, double y) -> double;
    auto printSomething() -> void;
    auto generateSubstring(const std::string &s, int start, int len) -> std::string;

Type deduction can't be used for function parameter types
**********************************************************

Unfortunately, type deduction doesn't work for function parameters, and prior to C++20, programs won't compile (an error is generated about function parameters not being able to have an auto type).

In C++20, the auto keyword was extended so that the above program will compile and function correctly. However, ``auto`` is not invoking type deduction in this case. Rather, it is triggering a different feature called **function templates** that was designed to actually handle such cases.

.. note::
    Further information about **function templates** can be found in later chapter :doc:`../chapter21/generic-programming-with-function-templates`.
