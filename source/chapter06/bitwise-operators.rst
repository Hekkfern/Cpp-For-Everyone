###################
Bitwise operators
###################

The bitwise operators
***********************

C++ provides 6 bit manipulation operators, often called **bitwise** operators:

+-------------+---------+------------+-------------------------------------+
| Operator    | Symbol  | Form       | Operation                           |
+=============+=========+============+=====================================+
| left shift  | ``<<``  | ``x << y`` | all bits in x shifted left y bits   |
+-------------+---------+------------+-------------------------------------+
| right shift | ``>>``  | ``x >> y`` | all bits in x shifted right y bits  |
+-------------+---------+------------+-------------------------------------+
| bitwise NOT | ``~``   | ``~x``     | all bits in x flipped               |
+-------------+---------+------------+-------------------------------------+
| bitwise AND | ``&``   | ``x & y``  | each bit in x AND each bit in y     |
+-------------+---------+------------+-------------------------------------+
| bitwise OR  | ``|``   | ``x | y``  | each bit in x OR each bit in y      |
+-------------+---------+------------+-------------------------------------+
| bitwise XOR | ``^``   | ``x ^ y``  | each bit in x XOR each bit in y     |
+-------------+---------+------------+-------------------------------------+

The bitwise operators are defined for integral types and std::bitset.

Avoid using the bitwise operators with signed operands, as many operators will return implementation-defined results prior to C++20 or have other potential gotchas that are easily avoided by using unsigned operands (or std::bitset).

Bitwise left shift (``<<``) and bitwise right shift (``>>``) operators
***********************************************************************

The bitwise left shift (``<<``) operator shifts bits to the left. The left operand is the expression to shift the bits of, and the right operand is an integer number of bits to shift left by.

So when ``x << N`` is written, it means "shift the bits in the variable x left by N places". New bits shifted in from the right side receive the value 0.

.. code-block:: none

    0011 << 1 is 0110
    0011 << 2 is 1100
    0011 << 3 is 1000

Bits that are shifted off the end of the binary number are lost forever.

The bitwise right shift (``>>``) operator shifts bits to the right.

.. code-block:: none

    1100 >> 1 is 0110
    1100 >> 2 is 0011
    1100 >> 3 is 0001

If a bit is shifted off the right end of the number, it is lost.

Bitwise NOT
************

The **bitwise NOT** operator (``~``) simply flips each bit from a 0 to a 1, or vice versa. Note that the result of a *bitwise NOT* is dependent on what size your data type is.

.. code-block:: none

    ~0100 is 1011
    ~0000 0100 is 1111 1011

Bitwise OR
************

*Bitwise OR* (``|``) works much like its *logical OR* counterpart. However, instead of applying the *OR* to the operands to produce a single result, *bitwise OR* applies to each bit.

To do (any) bitwise operations, it is easiest to line the two operands up like this, and then apply the operation to each column of bits.

.. code-block:: none

    0 1 0 1 OR
    0 1 1 0
    -------
    0 1 1 1

Programmatically, the same operation would be done as ``(std::bitset<4>{ 0b0101 } | std::bitset<4>{ 0b0110 })``.

The same thing can be done to compound OR expressions, such as ``0b0111 | 0b0011 | 0b0001``. If any of the bits in a column are 1, the result of that column is 1.

.. code-block:: none

    0 1 1 1 OR
    0 0 1 1 OR
    0 0 0 1
    --------
    0 1 1 1

And programmatically, the operation is represented as ``(std::bitset<4>{ 0b0111 } | std::bitset<4>{ 0b0011 } | std::bitset<4>{ 0b0001 })``.

Bitwise AND
************

*Bitwise AND* (``&``) works similarly to the above. *Logical AND* evaluates to true if both the left and right operand evaluate to true. *Bitwise AND* evaluates to true (1) if both bits in the column are 1.

.. code-block:: none

    0 1 0 1 AND
    0 1 1 0
    --------
    0 1 0 0

Which programmatically is represented as ``(std::bitset<4>{ 0b0101 } & std::bitset<4>{ 0b0110 })``.

Similarly, in a compound AND expression,  if all of the bits in a column are 1, the result of that column is 1.

.. code-block:: none
    
    0 0 0 1 AND
    0 0 1 1 AND
    0 1 1 1
    --------
    0 0 0 1

Which programmatically is represented as ``(std::bitset<4>{ 0b0001 } & std::bitset<4>{ 0b0011 } & std::bitset<4>{ 0b0111 })``.

Bitwise XOR
************

When evaluating two operands, XOR evaluates to true (1) if one and only one of its operands is true (1). If neither or both are true, it evaluates to 0. 

.. code-block:: none

    0 1 1 0 XOR
    0 0 1 1
    -------
    0 1 0 1

It is also possible to evaluate compound XOR expression column style, such as ``0b0001 ^ 0b0011 ^ 0b0111``. If there are an even number of 1 bits in a column, the result is 0. If there are an odd number of 1 bits in a column, the result is 1.

.. code-block:: none

    0 0 0 1 XOR
    0 0 1 1 XOR
    0 1 1 1
    --------
    0 1 0 1

Bitwise assignment operators
*****************************

Similar to the arithmetic assignment operators, C++ provides bitwise assignment operators in order to facilitate easy modification of variables.

+------------------------+---------+-------------+--------------------------+
| Operator               | Symbol  | Form        | Operation                |
+========================+=========+=============+==========================+
| Left shift assignment  | ``<<=`` | ``x <<= y`` | Shift x left by y bits   |
+------------------------+---------+-------------+--------------------------+
| Right shift assignment | ``>>=`` | ``x >>= y`` | Shift x right by y bits  |
+------------------------+---------+-------------+--------------------------+
| Bitwise OR assignment  | ``|=``  | ``x |= y``  | Assign ``x | y`` to x    |
+------------------------+---------+-------------+--------------------------+
| Bitwise AND assignment | ``&=``  | ``x &= y``  | Assign ``x & y`` to x    |
+------------------------+---------+-------------+--------------------------+
| Bitwise XOR assignment | ``^=``  | ``x ^= y``  | Assign ``x ^ y`` to x    |
+------------------------+---------+-------------+--------------------------+

For example, instead of writing ``x = x >> 1;``, ``x >>= 1;`` is equivalent.
