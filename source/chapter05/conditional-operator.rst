######################
Conditional operator
######################

The conditional operator
************************

+--------------+---------+---------------+---------------------------------------------------------------+
| Operator     | Symbol  | Form          | Operation                                                     |
+==============+=========+===============+===============================================================+
| Conditional  | ``?:``  | ``c ? x : y`` | If c is nonzero (true) then evaluate x, otherwise evaluate y  |
+--------------+---------+---------------+---------------------------------------------------------------+

The **conditional operator** (``?:``) (also sometimes called the “arithmetic if” operator) is a ternary operator (it takes 3 operands). Because it has historically been C++'s only ternary operator, it's also sometimes referred to as “the ternary operator”.

The ``?:`` operator provides a shorthand method for doing a particular type of if/else statement.

An if/else statement takes the following form:

.. code-block:: cpp
    :linenos:

    if (condition)
        statement1;
    else
        statement2;

If *condition* evaluates to true, then *statement1* is executed, otherwise *statement2* is executed.

The ``?:`` operator takes the following form:

.. code-block:: cpp

    (condition) ? expression1 : expression2;

If *condition* evaluates to true, then *expression1* is executed, otherwise *expression2* is executed. Note that *expression2* is not optional.

The conditional operator can help compact code without losing readability.

Parenthesization of the conditional operator
***********************************************

It is common convention to put the conditional part of the operation inside of parentheses, both to make it easier to read, and also to make sure the precedence is correct. The other operands evaluate as if they were parenthesized, so explicit parenthesization is not required for those.

Note that the ``?:`` operator has a very low precedence. If doing anything other than assigning the result to a variable, the whole ``?:`` operator also needs to be wrapped in parentheses.

For example:

.. code-block:: cpp

    std::cout << ((x > y) ? x : y);

The conditional operator evaluates as an expression
****************************************************

Because the conditional operator operands are expressions rather than statements, the conditional operator can be used in some places where if/else can not.

For example, when initializing a constant variable:

.. code-block:: cpp
    :linenos:

    int main()
    {
        constexpr bool inBigClassroom { false };
        constexpr int classSize { inBigClassroom ? 30 : 20 };
        std::cout << "The class size is: " << classSize << '\n';

        return 0;
    }

The type of the expressions must match or be convertible
**********************************************************

To properly comply with C++'s type checking, either the type of both expressions in a conditional statement must match, or the both expressions must be convertible to a common type.

For example, this code won't compile:

.. code-block:: cpp
    :linenos:

    int main()
    {
        constexpr int x{ 5 };
        std::cout << (x != 5 ? x : "x is 5"); // won't compile

        return 0;
    }

The above example won't compile because one of the expressions is an integer, and the other is a string literal. The compiler is unable to determine a common type for expressions of these types. In such cases, if/else structure must be used.
