######################
What is an Operator?
######################

Operators
**********

In mathematics, an **operation** is a mathematical calculation involving zero or more input values (called **operands**) that produces a new value (called an output value). The specific operation to be performed is denoted by a construct (typically a symbol or pair of symbols) called an **operator**.

The number of operands that an operator takes as input is called the operator's **arity**:abbr:

* **Unary** operators act on one operand. An example of a unary operator is the ``-`` operator. For example, given -5, *operator-* takes literal operand 5 and flips its sign to produce new output value -5.

* **Binary** operators act on two operands (known as left and right). An example of a binary operator is the ``+`` operator. For example, given ``3 + 4``, *operator+* takes the left operand (3) and the right operand (4) and applies mathematical addition to produce new output value 7. The insertion (``<<``) and extraction (``>>``) operators are binary operators, taking ``std::cout`` or ``std::cin`` on the left side, and the item to output or variable to input to on the right side.

* **Ternary** operators act on three operands.

Note that some operators have more than one meaning depending on how they are used. For example, operator- has two contexts. It can be used in unary form to invert a number's sign (e.g. to convert 5 to -5, or vice versa), or it can be used in binary form to do subtraction (e.g. ``4 - 3``).

Chaining operators
*******************

Operators can be chained together such that the output of one operator can be used as the input for another operator. However, order of the operands must be taken into account.
