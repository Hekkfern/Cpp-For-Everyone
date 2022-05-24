#########################
Functions and constants
#########################

Constexpr functions
*********************

A **constexpr function** is a function whose return value may be computed at compile-time. To make a function a constexpr function, we simply use the ``constexpr`` keyword in front of the return type.

.. code-block:: cpp
    :linenos:

    constexpr int greater(int x, int y) // now a constexpr function
    {
        return (x > y ? x : y);
    }

    int main()
    {
        constexpr int x{ 5 };
        constexpr int y{ 6 };

        constexpr int g { greater(x, y) }; // will be evaluated at compile-time

        std::cout << g << " is greater!";

        return 0;
    }

To be eligible for compile-time evaluation, a function must have a constexpr return type and not call any non-constexpr functions. Additionally, a call to the function must have constexpr arguments (e.g. constexpr variables or literals).

Constexpr functions are implicitly inline
********************************************

Because constexpr functions may be evaluated at compile-time, the compiler must be able to see the full definition of the constexpr function at all points where the function is called.

This means that a constexpr function called in multiple files needs to have its definition included into each such file, which would normally be a violation of the one-definition rule. To avoid such problems, constexpr functions are implicitly inline, which makes them exempt from the one-definition rule.

As a result, constexpr functions are often defined in header files, so they can be #included into any .cpp file that requires the full definition.

Constexpr functions can also be evaluated at runtime
*****************************************************

Functions with a constexpr return value can also be evaluated at runtime, in which case they will return a non-constexpr result.

.. code-block:: cpp
    :linenos:

    constexpr int greater(int x, int y)
    {
        return (x > y ? x : y);
    }

    int main()
    {
        int x{ 5 }; // not constexpr
        int y{ 6 }; // not constexpr

        std::cout << greater(x, y) << " is greater!"; // will be evaluated at runtime

        return 0;
    }

If the function arguments are not constexpr, the function cannot be resolved at compile-time. However, the function will still be resolved at runtime, returning the expected value as a non-constexpr.

According to the C++ standard, a constexpr function that is eligible for compile-time evaluation must be evaluated at compile-time if the return value is used where a constant expression is required. Otherwise, the compiler is free to evaluate the function at either compile-time or runtime.

Let's examine a few cases to explore this further:

.. code-block:: cpp
    :linenos:

    constexpr int greater(int x, int y)
    {
        return (x > y ? x : y);
    }

    int main()
    {
        constexpr int g { greater(5, 6) };            // case 1: evaluated at compile-time
        std::cout << g << "is greater!";

        int x{ 5 }; // not constexpr
        std::cout << greater(x, 6) << " is greater!"; // case 2: evaluated at runtime

        std::cout << greater(5, 6) << " is greater!"; // case 3: may be evaluated at either runtime or compile-time

        return 0;
    }

In case 1, ``greater()`` is being called with constexpr arguments, so it is eligible to be evaluated at compile-time. The initializer of constexpr variable ``g`` must be a constant expression, so the return value is used in a context that requires a constant expression. Thus, ``greater()`` must be evaluated at compile-time.

In case 2, ``greater()`` is being called with one parameter that is non-constexpr. Thus ``greater()`` cannot be evaluated at compile-time, and must evaluate at runtime.

Case 3 is the interesting case. The ``greater()`` function is again being called with constexpr arguments, so it is eligible for compile-time evaluation. However, the return value is not being used in a context that requires a constant expression (``operator<<`` always executes at runtime), so the compiler is free to choose whether this call to ``greater()`` will be evaluated at compile-time or runtime!

Note that the compiler's optimization level setting may have an impact on whether it decides to evaluate a function at compile-time or runtime. This also means that the compiler may make different choices for debug vs. release builds (as debug builds typically have optimizations turned off).

Forcing a constexpr function to be evaluated at compile-time
**************************************************************

There is no way to tell the compiler that a constexpr function should prefer to evaluate at compile-time whenever it can (even in cases where the return value is used in a non-constant expression).

However, we can force a constexpr function that is eligible to be evaluated at compile-time to actually evaluate at compile-time by ensuring the return value is used where a constant expression is required. This needs to be done on a per-call basis.

The most common way to do this is to use the return value to initialize a constexpr variable. Unfortunately, this requires introducing a new variable into the program just to ensure compile-time evaluation, which is ugly and reduces code readability.

However, in C++20, there is a better workaround to this issue: C++20 introduces the keyword ``consteval``, which is used to indicate that a function *must* evaluate at compile-time, otherwise a compile error will result. Such functions are called **immediate functions**.

.. code-block:: cpp
    :linenos:

    consteval int greater(int x, int y) // function is now consteval
    {
        return (x > y ? x : y);
    }

    int main()
    {
        constexpr int g { greater(5, 6) };            // ok: will evaluate at compile-time
        std::cout << greater(5, 6) << " is greater!"; // ok: will evaluate at compile-time

        int x{ 5 }; // not constexpr
        std::cout << greater(x, 6) << " is greater!"; // error: consteval functions must evaluate at compile-time

        return 0;
    }

Just like constexpr functions, consteval functions are implicitly inline.

The downside of consteval functions is that such functions can't evaluate at runtime, making them less flexible than constexpr functions, which can do either.

Therefore, it would still be useful to have a convenient way to force constexpr functions to evaluate at compile-time (even when the return value is being used where a constant expression is not required), so that having compile-time evaluation when possible, and runtime evaluation otherwise.

Consteval functions provides a way to make this happen, using a neat helper function:

.. code-block:: cpp
    :linenos:

    // Uses abbreviated function template (C++20) and `auto` return type to make this function work with any type of value
    consteval auto compileTime(auto value)
    {
        return value;
    }

    constexpr int greater(int x, int y) // function is constexpr
    {
        return (x > y ? x : y);
    }

    int main()
    {
        std::cout << greater(5, 6);              // may or may not execute at compile-time
        std::cout << compileTime(greater(5, 6)); // will execute at compile-time

        int x { 5 };
        std::cout << greater(x, 6);              // we can still call the constexpr version at runtime if we wish

        return 0;
    }

This works because consteval functions require constant expressions as arguments; therefore, if the return value of a constexpr function is used as an argument to a consteval function, the constexpr function must be evaluated at compile-time. The consteval function just returns this argument as its own return value, so the caller can still use it.

Note that the consteval function returns by value. While this might be inefficient to do at runtime (if the value was some type that is expensive to copy, e.g. std::string), in a compile-time context, it doesn't matter because the entire call to the consteval function will simply be replaced with the calculated return value.
