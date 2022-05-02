###################################################
4.2 Integer signedness
###################################################

Signed integers
***********************************

By default, integers are **signed**, which means the number's sign is stored as part of the number (using a single bit called the **sign bit**). Therefore, a signed integer can hold both positive and negative numbers (and 0).

**Two's complement** is the most common method of representing signed integers on computers, and more generally, fixed point binary values.

This system has the advantage that the fundamental arithmetic operations of addition, subtraction, and multiplication are identical to those for unsigned binary numbers (as long as the inputs are represented in the same number of bits as the output, and any overflow beyond those bits is discarded from the result). Also, it has no representation for negative zero, and thus does not suffer from its associated difficulties.

A way of finding the two's complement of a number is to take its ones' complement (permute the value of all its bits from ``0`` to ``1``, and viceversa) and add one.

For example, in a 4-bit signed integer, ``-4`` is represented as ``1100``:

#. ``0100`` (binary representation for the positive value)
#. ``1011`` (one's complement)
#. ``1100`` (add one)

For more information about "Two's complement", read `Wikipedia <https://en.wikipedia.org/wiki/Two%27s_complement>`_.

The preferred way to define the four types of signed integers:

.. code-block:: cpp

    short s;
    int i;
    long l;
    long long ll;

The integer types can also take an optional ``signed`` keyword, which by convention is typically placed before the type name. However, this keyword should not be used, as it is redundant, since integers are signed by default.

.. code-block:: cpp

    signed short ss;
    signed int si;
    signed long sl;
    signed long long sll;

Unsigned integers
******************

**Unsigned integers** are integers that can only hold non-negative whole numbers.

To define an unsigned integer, the ``unsigned`` keyword is used. By convention, this is placed before the type.

.. code-block:: cpp

    unsigned short us;
    unsigned int ui;
    unsigned long ul;
    unsigned long long ull;

Integer ranges
***************

The set of specific values that a data type can hold is called range.

Signed integers
================

+---------------+----------------------------------------------------------+
| Size/Type     | Range                                                    |
+===============+==========================================================+
| 8 bit signed  | -128 to 127                                              |
+---------------+----------------------------------------------------------+
| 16 bit signed | -32,768 to 32,767                                        |
+---------------+----------------------------------------------------------+
| 32 bit signed | -2,147,483,648 to 2,147,483,647                          |
+---------------+----------------------------------------------------------+
| 64 bit signed | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807  |
+---------------+----------------------------------------------------------+

For the math inclined, an n-bit signed variable has a range of :math:`-2^{n-1}` to :math:`2^{n-1}-1`.

Unsigned integers
==================

+-----------------+----------------------------------+
| Size/Type       | Range                            |
+=================+==================================+
| 8 bit unsigned  | 0 to 255                         |
+-----------------+----------------------------------+
| 16 bit unsigned | 0 to 65,535                      |
+-----------------+----------------------------------+
| 32 bit unsigned | 0 to 4,294,967,295               |
+-----------------+----------------------------------+
| 64 bit unsigned | 0 to 18,446,744,073,709,551,615  |
+-----------------+----------------------------------+

For the math inclined, an n-bit signed variable has a range of :math:`0` to :math:`2^{n-1}`.

**Integer overflow** (often called **overflow** for short) occurs when a value that is outside the range of the type is tried to be stored. Essentially, the number tried to be stored requires more bits to represent than the object has available. In such a case, data is lost because the object does not have enough memory to store everything.

In the case of signed integers, which bits are lost is not well defined, thus signed integer overflow leads to undefined behavior.

If an unsigned value is out of range, it is divided by one greater than the largest number of the type, and only the remainder kept. Any number bigger than the largest number representable by the type simply “wraps around” (sometimes called “modulo wrapping”).
