#########################################
Value categories (L-values and R-values)
#########################################

Introduction
*************

An **expression** in C++ is “a combination of literals, variables, operators, and function calls that can be executed to produce a singular value”.

All expressions in C++ have two properties: a **type** and a **value category**.

The type of an expression
**************************

The **type of an expression** is equivalent to the type of the value, object, or function that results from the evaluated expression.

For example:

.. code-block:: cpp
    :linenos:

    auto v1 { 12 / 4 }; // int / int => int
    auto v2 { 12.0 / 4 }; // double / int => double

For ``v1``, the compiler will determine (at compile time) that a division with two ``int`` operands will produce an ``int`` result, so ``int`` is the type of this expression. Via type inference, ``int`` will then be used as the type of ``v1``.

For ``v2``, the compiler will determine (at compile time) that a division with a ``double`` operand and an ``int`` operand will produce a ``double`` result. Remember that arithmetic operators must have operands of matching types, so in this case, the ``int`` operand gets converted to a ``double``, and a floating point division is performed. So ``double`` is the type of this expression.

The compiler can use the type of an expression to determine whether an expression is valid in a given context.

For example:

.. code-block:: cpp
    :linenos:

    void print(int x)
    {
        std::cout << x << '\n';
    }

    int main()
    {
        print("foo"); // error: print() was expecting an int argument, we tried to pass in a string literal

        return 0;
    }

In the above program, the ``print(int)`` function is expecting an ``int`` parameter. However, the type of the expression it is receiving (the string literal ``"foo"``) does not match, and no conversion can be found. So a compile error results.

Note that the type of an expression must be determinable at compile time (otherwise type checking and type deduction wouldn't work). However, the value of an expression may be determined at either compile time (if the expression is ``constexpr``) or runtime (if the expression is not ``constexpr``).

The value category of an expression
*************************************

Now consider the following program:

.. code-block:: cpp
    :linenos:

    int main()
    {
        int x{};

        x = 5; // valid: we can assign 5 to x
        5 = x; // error: can not assign value of x to literal value 5

        return 0;
    }

One of these assignment statements is valid (assigning value ``5`` to variable ``x``) and one is not (what would it mean to assign the value of ``x`` to the literal value ``5``?). So how does the compiler know which expressions can legally appear on either side of an assignment statement?

The answer lies in the second property of expressions: the value category. The **value category** of an expression (or subexpression) indicates whether an expression resolves to a value, a function, or an object of some kind.

Prior to C++11, there were only two possible value categories: ``lvalue`` and ``rvalue``.

In C++11, three additional value categories (``glvalue``, ``prvalue``, and ``xvalue``) were added to support a new feature called **move semantics**.

.. note::

    Move semantics  (and the additional three value categories) will be covered in a future chapter :doc:`../chapter14/move-semantics`

Lvalue and rvalue expressions
*******************************

An **lvalue** (pronounced “ell-value”, short for “left value” or “locator value”, and sometimes written as “l-value”) is an expression that evaluates to an identifiable object or function (or bit-field).

The term “identity” is used by the C++ standard, but is not well-defined. An entity (such as an object or function) that has an identity can be differentiated from other similar entities (typically by comparing the addresses of the entity).

Entities with identities can be accessed via an identifier, reference, or pointer, and typically have a lifetime longer than a single expression or statement.

.. code-block:: cpp
    :linenos:

    int x { 5 };
    int y { x }; // x is an lvalue expression

In the above program, the expression ``x`` is an lvalue expression as it evaluates to variable ``x`` (which has an identifier).

Since the introduction of constants into the language, lvalues come in two subtypes: a **modifiable lvalue** is an lvalue whose value can be modified. A **non-modifiable lvalue** is an lvalue whose value can't be modified (because the lvalue is const or constexpr).

.. code-block:: cpp
    :linenos:

    int x{};
    const double d{};

    int y { x }; // x is a modifiable lvalue expression
    const double e { d }; // d is a non-modifiable lvalue expression

An **rvalue** (pronounced “arr-value”, short for “right value”, and sometimes written as "r-value") is an expression that is not an l-value. Commonly seen rvalues include literals (except C-style string literals, which are lvalues) and the return value of functions and operators. Rvalues aren't identifiable (meaning they have to be used immediately), and only exist within the scope of the expression in which they are used.

.. code-block:: cpp
    :linenos:

    int x{ 5 }; // 5 is an rvalue expression
    const double d{ 1.2 }; // 1.2 is an rvalue expression

    int y { x }; // x is a modifiable lvalue expression
    const double e { d }; // d is a non-modifiable lvalue expression
    int z { return5() }; // return5() is an rvalue expression (since the result is returned by value)

    int w { x + 1 }; // x + 1 is an rvalue expression
    int q { static_cast<int>(d) }; // the result of static casting d to an int is an rvalue expression

Why ``return5()``, ``x + 1``, and ``static_cast<int>(d)`` are rvalues? The answer is because these expressions produce temporary values that are not identifiable objects.

Now the question about why ``x = 5`` is valid but ``5 = x`` is not can be answered: an assignment operation requires the left operand of the assignment to be a modifiable lvalue expression, and the right operand to be an rvalue expression. The latter assignment (``5 = x``) fails because the left operand expression ``5`` isn't an lvalue.

.. code-block:: cpp
    :linenos:

    // Assignment requires the left operand to be a modifiable lvalue expression and the right operand to be an rvalue expression
    x = 5; // valid: x is a modifiable lvalue expression and 5 is an rvalue expression
    5 = x; // error: 5 is an rvalue expression and x is a modifiable lvalue expression

.. note::

    A full list of lvalue and rvalue expressions can be found `here <https://en.cppreference.com/w/cpp/language/value_category>`_. In C++11, rvalues are broken into two subtypes: prvalues and xvalues, so the rvalues talked about in this lesson are the sum of both of those categories.

.. note::

    As a rule of thumb to identify lvalue and rvalue expressions:

    * lvalues expressions are those that evaluate to variables or other identifiable objects that persist beyond the end of the expression.
    * rvalues expressions are those that evaluate to literals or the returned value of functions and operators that are discarded at the end of the expression.

L-value to r-value conversion
*******************************

Lvalues will implicitly convert to rvalues, so an lvalue can be used wherever an rvalue is required.

So, the next piece of code is correct:

.. code-block:: cpp
    :linenos:

    int x{ 1 };
    int y{ 2 };

    x = y; // y is a modifiable lvalue, not an rvalue, but this is legal

Now consider this snippet:

.. code-block:: cpp
    :linenos:

    int x { 2 };

    x = x + 1;

In this statement, the variable ``x`` is being used in two different contexts. On the left side of the assignment operator, ``x`` is an lvalue expression that evaluates to variable x. On the right side of the assignment operator, ``x + 1`` is an rvalue expression that evaluates to the value ``3``.
