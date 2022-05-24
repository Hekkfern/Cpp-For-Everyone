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

Don't add unnecessary == or != to conditions. It makes them harder to read without offering any additional value.

Avoid using operator== and operator!= with floating point operands.

When mixing logical AND and logical OR in a single expression, explicitly parenthesize each operation to ensure they evaluate how you intend.

To avoid surprises, use the bitwise operators with unsigned operands or std::bitset.

Avoid using-directives (such as using namespace std;) at the top of your program or in header files. They violate the reason why namespaces were added in the first place.

Local variables inside the function body should be defined as close to their first use as reasonable

Define variables in the most limited existing scope. Avoid creating new blocks whose only purpose is to limit the scope of variables.

Consider using a `g` or `g_` prefix for global variables to help differentiate them from local variables.

Use of non-constant global variables should generally be avoided.

Shadowing of local variables should generally be avoided, as it can lead to inadvertent errors where the wrong variable is used or modified.

Do not use the ``inline`` keyword to request inline expansion for your functions.

Consider putting single statements associated with an if or else in blocks (``{ }``).

Prefer ``switch statements`` over ``if-else`` chains when there is a choice.

In ``switch statements``, each set of statements underneath a label should end in a ``break statement`` or a ``return statement``.

Avoid ``goto statements`` (unless the alternatives are significantly worse for code readability).
