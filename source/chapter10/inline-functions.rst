#######################
Inline functions
#######################

Introduction
*************

One downside of using a function is that every time a function is called, there is a certain amount of performance overhead that occurs.

For functions that are large and/or perform complex tasks, the overhead of the function call is typically insignificant compared to the amount of time the function takes to run. However, for small functions, the overhead costs can be larger than the time needed to actually execute the function's code. In cases where a small function is called often, using a function can result in a significant performance penalty over writing the same code in-place.

Inline expansion
*****************

**Inline expansion** is a process where a function call is replaced by the code from the called function's definition.

Note that two calls to an inline function generate two replacements of the function call (with the value of the arguments substituted for the parameters).

However, inline expansion has its own potential cost: if the body of the function being expanded takes more instructions than the function call being replaced, then each inline expansion will cause the executable to grow larger. Larger executables tend to be slower (due to not fitting as well in caches).

The decision about whether a function would benefit from being made inline (because removal of the function call overhead outweighs the cost of a larger executable) is not straightforward. Inline expansion could result in performance improvements, performance reductions, or no change to performance at all, depending on the relative cost of a function call, the size of the function, and what other optimizations can be performed.

Inline expansion is best suited to simple, short functions (e.g. no more than a few statements), especially cases where a single function call is executed more than once (e.g. function calls inside a loop).

Every function falls into one of three categories, where calls to the function:

* Must be expanded.
* May be expanded (most functions are in this category).
* Can't be expanded.

A function that is eligible to have its function calls expanded is called an **inline function**.

Most functions fall into the “may” category: their function calls can be expanded if and when it is beneficial to do so. For functions in this category, a modern compiler will assess each function and each function call to make a determination about whether that particular function call would benefit from inline expansion. A compiler might decide to expand none, some, or all of the function calls to a given function.

The inline keyword
*******************

Historically, compilers either didn't have the capability to determine whether inline expansion would be beneficial, or were not very good at it. For this reason, C++ provides the keyword inline, which was intended to be used as a hint to the compiler that a function would benefit from being expanded inline:

.. code-block:: cpp
    :linenos:

    inline int min(int x, int y) // hint to the compiler that it should do inline expansion of this function
    {
        return (x < y) ? x : y;
    }

    int main()
    {
        std::cout << min(5, 6) << '\n';
        std::cout << min(3, 2) << '\n';
        return 0;
    }

This is where the term “inline function” comes from (because such functions had the ``inline`` specifier as part of the declaration syntax of the function).

However, in modern C++, the inline keyword is no longer used to request that a function be expanded inline. There are quite a few reasons for this:

* Using inline to request inline expansion is a form of premature optimization, and misuse could actually harm performance.
* The inline keyword is just a hint, the compiler is completely free to ignore a request to inline a function. The compiler is also free to perform inline expansion of functions that do not use the inline keyword as part of its normal set of optimizations.
* The inline keyword is defined at the wrong level of granularity. We use the inline keyword on a function declaration, but inline expansion is actually determined per function call. It may be beneficial to expand some function calls and detrimental to expand others, and there is no syntax to affect this.

Modern optimizing compilers are typically very good at determining which functions should be made inline, better than humans in most cases. As a result, the compiler will likely ignore or devalue any request the developer make to inline a function anyway.

In modern C++, the ``inline`` concept has evolved to have a new meaning: multiple definitions are allowed in the program. If a function is marked as inline, then that function is allowed to have multiple definitions (in different files), as long as those definitions are identical. This is true for functions as well as variables.

In order to do inline expansion, the compiler needs to be able to see the full definition of an inline function wherever the function is called. Therefore, inline functions are typically defined in header files, where they can be #included into any code file that needs to see the full definition of the function.
