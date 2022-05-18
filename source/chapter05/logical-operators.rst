######################
Logical operators
######################

Introduction
*************

While relational (comparison) operators can be used to test whether a particular condition is true or false, they can only test one condition at a time. Often the code needs to know whether multiple conditions are true simultaneously.

Logical operators provide the capability to test multiple conditions.

C++ has 3 logical operators:

+--------------+---------+------------+--------------------------------------------------+
| Operator     | Symbol  | Form       | Operation                                        |
+==============+=========+============+==================================================+
| Logical NOT  | ``!``   | ``!x``     | true if x is false, or false if x is true        |
+--------------+---------+------------+--------------------------------------------------+
| Logical AND  | ``&&``  | ``x && y`` | true if both x and y are true, false otherwise   |
+--------------+---------+------------+--------------------------------------------------+
| Logical OR   | ``||``  | ``x || y`` | true if either x or y are true, false otherwise  |
+--------------+---------+------------+--------------------------------------------------+

Logical NOT
************

If *logical NOT*'s operand evaluates to true, logical NOT evaluates to false. If *logical NOT*'s operand evaluates to false, logical NOT evaluates to true. In other words, logical NOT flips a Boolean value from true to false, and vice-versa.

+---------------------------+---------+
| Logical NOT (operator ``!``)        |
+---------------------------+---------+
| Operand                   | Result  |
+===========================+=========+
| true                      | false   |
+---------------------------+---------+
| false                     | true    |
+---------------------------+---------+

One thing to be wary of is that logical NOT has a very high level of precedence. So ``if (!x > y)...`` actually evaluates as ``if ((!x) > y) ..``.

Simple uses of logical NOT, such as ``if (!value)`` do not need parentheses because precedence does not come into play.

Logical OR
***********

The *logical OR* operator is used to test whether either of two conditions is true. If the left operand evaluates to true, or the right operand evaluates to true, or both are true, then the logical OR operator returns true. Otherwise it will return false.

+---------------------------+----------------+---------+
| Logical OR (operator ``||``)                         |
+---------------------------+----------------+---------+
| Left operand              | Right operand  | Result  |
+===========================+================+=========+
| false                     | false          | false   |
+---------------------------+----------------+---------+
| false                     | true           | true    |
+---------------------------+----------------+---------+
| true                      | false          | true    |
+---------------------------+----------------+---------+
| true                      | true           | true    |
+---------------------------+----------------+---------+

Many *logical OR* statements can be chained:

.. code-block:: cpp
    :linenos:

    if (value == 0 || value == 1 || value == 2 || value == 3)
        std::cout << "You picked 0, 1, 2, or 3\n";


Be careful not to confuse the *logical OR* operator (``||``) with the *bitwise OR* operator (``|``). Even though they both have "OR" in the name, they perform different functions. Mixing them up will probably lead to incorrect results.

Logical AND
************

The *logical AND* operator is used to test whether both operands are true. If both operands are true, logical AND returns true. Otherwise, it returns false.

+---------------------------+----------------+---------+
| Logical AND (operator ``&&``)                        |
+---------------------------+----------------+---------+
| Left operand              | Right operand  | Result  |
+===========================+================+=========+
| false                     | false          | false   |
+---------------------------+----------------+---------+
| false                     | true           | false   |
+---------------------------+----------------+---------+
| true                      | false          | false   |
+---------------------------+----------------+---------+
| true                      | true           | true    |
+---------------------------+----------------+---------+

As with logical OR, you can string together many logical AND statements:

.. code-block:: cpp
    :linenos:

    if (value > 10 && value < 20 && value != 16)
        // do something
    else
        // do something else

As with logical and bitwise OR, don't confuse the *logical AND* operator (``&&``) with the *bitwise AND* operator (``&``).

Short circuit evaluation
*************************

In order for *logical AND* to return true, both operands must evaluate to true. If the first operand evaluates to false, *logical AND* knows it must return false regardless of whether the second operand evaluates to true or false. In this case, the *logical AND* operator will go ahead and return false immediately without even evaluating the second operand! This is known as **short circuit evaluation**, and it is done primarily for optimization purposes.

Similarly, if the first operand for *logical OR* is true, then the entire OR condition has to evaluate to true, and the second operand won't be evaluated.

Short circuit evaluation presents another opportunity to show why operators that cause side effects should not be used in compound expressions.

Consider the following snippet:

.. code-block:: cpp
    :linenos:

    if (x == 1 && ++y == 2)
        // do something

if ``x`` does not equal ``1``, the whole condition must be false, so ``++y`` never gets evaluated! Thus, ``y`` will only be incremented if ``x`` evaluates to ``1``, which is probably not what the programmer intended!

The *logical OR* and *logical AND* operators are an exception to the rule that the operands may evaluate in any order, as the standard explicitly states that the left operand must evaluate first.

Only the built-in versions of these operators perform short-circuit evaluation. If you overload these operators to make them work with your own types, those overloaded operators will not perform short-circuit evaluation.

Mixing ANDs and ORs
********************

Mixing *logical AND* and *logical OR* operators in the same expression often can not be avoided, but it is an area full of potential dangers.

Many programmers assume that *logical AND* and *logical OR* have the same precedence (or forget that they don't), just like addition/subtraction and multiplication/division do. However, *logical AND* has higher precedence than *logical OR*, thus *logical AND* operators will be evaluated ahead of *logical OR* operators (unless they have been parenthesized).

When mixing logical AND and logical OR in the same expression, it is a good idea to explicitly parenthesize each operator and its operands. This helps prevent precedence mistakes, makes your code easier to read, and clearly defines how you intended the expression to evaluate. For example, rather than writing ``value1 && value2 || value3 && value4``, it is better to write ``(value1 && value2) || (value3 && value4)``.

De Morgan's law
****************

Many programmers also make the mistake of thinking that ``!(x && y)`` is the same thing as ``!x && !y``.

`De Morgan's law <https://en.wikipedia.org/wiki/De_Morgan%27s_laws>`_ tells how the *logical NOT* should be distributed in these cases:

* ``!(x && y)`` is equivalent to ``!x || !y``
* ``!(x || y)`` is equivalent to ``!x && !y``

In other words, when the *logical NOT* needs to be distributed, flipping *logical AND* to *logical OR*, and vice-versa, is required.

+--------+--------+--------+--------+---------------+--------------+---------------+--------------+
| ``x``  | ``y``  | ``!x`` | ``!y`` | ``!(x && y)`` | ``!x || !y`` | ``!(x || y)`` | ``!x && !y`` |
+========+========+========+========+===============+==============+===============+==============+
| false  | false  | true   | true   | true          | true         | true          | true         |
+--------+--------+--------+--------+---------------+--------------+---------------+--------------+
| false  | true   | true   | false  | true          | true         | false         | false        |
+--------+--------+--------+--------+---------------+--------------+---------------+--------------+
| true   | false  | false  | true   | true          | true         | false         | false        |
+--------+--------+--------+--------+---------------+--------------+---------------+--------------+
| true   | true   | false  | false  | false         | false        | false         | false        |
+--------+--------+--------+--------+---------------+--------------+---------------+--------------+

Where's the logical exclusive or (XOR) operator?
*************************************************

*Logical XOR* is a logical operator provided in some languages that is used to test whether an odd number of conditions is true.

+--------------+----------------+----------+
| Logical XOR                              |
+--------------+----------------+----------+
| Left operand | Right operand  | Result   |
+==============+================+==========+
| false        | false          | false    |
+--------------+----------------+----------+
| false        | true           | true     |
+--------------+----------------+----------+
| true         | false          | true     |
+--------------+----------------+----------+
| true         | true           | false    |
+--------------+----------------+----------+

C++ doesn't provide a *logical XOR* operator. Unlike *logical OR* or *logical AND*, *logical XOR* cannot be short circuit evaluated. Because of this, making a *logical XOR* operator out of *logical OR* and *logical AND* operators is challenging. However, you can easily mimic *logical XOR* using the inequality operator (``!=``):

.. code-block:: cpp

    if (a != b) ... // a XOR b, assuming a and b are Booleans

This can be extended to multiple operands as follows:

.. code-block:: cpp

    if (a != b != c != d) ... // a XOR b XOR c XOR d, assuming a, b, c, and d are Booleans

Note that the above XOR patterns only work if the operands are Booleans (not integers). If a form of logical XOR that works with non-Boolean operands is needed, use ``static_cast`` to convert them to ``bool``.


Alternative operator representations
*************************************

Many operators in C++ (such as operator ``||``) have names that are just symbols. Historically, not all keyboards and language standards have supported all of the symbols needed to type these operators. As such, C++ supports an alternative set of keywords for the operators that use words instead of symbols. For example, instead of ``||``, you can use the keyword ``or``.

The full list can be found `here <https://en.cppreference.com/w/cpp/language/operator_alternative>`_. Of particular note are the following three:

+----------------+--------------------------+
| Operator name  | Keyword alternate name   |
+================+==========================+
| ``&&``         | ``and``                  |
+----------------+--------------------------+
| ``||``         | ``or``                   |
+----------------+--------------------------+
| ``!``          | ``not``                  |
+----------------+--------------------------+

This means the following are identical:

.. code-block:: cpp
    :linenos:

    std::cout << !a && (b || c);
    std::cout << not a and (b or c);

While these alternative names might seem easier to understand right now, most experienced C++ developers prefer using the symbolic names over the keyword names.
