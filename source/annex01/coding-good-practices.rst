####################################
Coding good practices
####################################

Although the language allows you to define multiples variables, avoid defining multiple variables in a single statement (even if they are the same type). Instead, define each variable in a separate statement (and then use a single-line comment to document what it is used for).

Favor initialization using braces whenever possible.

Any variable that should not be modifiable after initialization and whose initializer is known at compile-time should be declared as ``constexpr``. Any variable that should not be modifiable after initialization and whose initializer is not known at compile-time should be declared as ``const``.

Avoid using ``#define`` to create symbolic constants macros. Use ``const`` or ``constexpr`` variables instead.

Avoid magic numbers in your code (use symbolic constants instead).

Prefer ``int`` when the size of the integer doesn't matter. Prefer ``std::int#_t`` when storing a quantity that needs a guaranteed range. Prefer ``std::uint#_t`` when doing bit manipulation or where well-defined wrap-around behavior is required.

Avoid using:
* Unsigned types for holding quantities
* The 8-bit fixed-width integer types
* The fast and least fixed-width types
* Any compiler-specific fixed-width integers (for example, Visual Studio defines ``__int8``, ``__int16``, etc...)

Favor double over float unless space is at a premium, as the lack of precision in a float will often lead to inaccuracies.

Functions that return boolean values should be named starting with the word *is* (e.g. isEqual) or *has* (e.g. hasCommonDivisor).

Avoid const casts and reinterpret casts unless you have a very good reason to use them.

Avoid using C-style casts. Favor static_cast when you need to convert a value from one type to another type.

Favor explicit return types over function return type deduction for normal functions.

Use parentheses to make it clear how a non-trivial expression should evaluate (even if they are technically unnecessary). In order to reduce mistakes and make your code easier to understand without referencing a precedence table, it's a good idea to parenthesize any non-trivial compound expression, so it's clear what your intent is.

Strongly favor the prefix version of the increment and decrement operators, as they are generally more performant, and you're less likely to run into strange issues with them.

Always parenthesize the conditional part of the conditional operator (``?:``), and consider parenthesizing the whole thing as well.

Only use the conditional operator (``?:``) for simple conditionals where you use the result and where it enhances readability.
