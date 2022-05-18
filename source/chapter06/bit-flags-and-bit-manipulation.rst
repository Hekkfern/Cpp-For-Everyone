#################################################
Bit flags and bit manipulation via std::bitset
#################################################

Introduction
*************

C++ gives tools to manipulate objects at the bit level. Modifying individual bits within an object is called **bit manipulation**.

Bit flags
***********

When individual bits of an object are used as Boolean values, the bits are called **bit flags**.

To define a set of bit flags, an unsigned integer of the appropriate size (8 bits, 16 bits, 32 bits, etc… depending on how many flags we have), or ``std::bitset``, are typically used.

.. code-block:: cpp
    :linenos:

    #include <bitset> // for std::bitset

    std::bitset<8> mybitset {}; // 8 bits in size means room for 8 flags

Bit numbering and bit positions
********************************

Given a sequence of bits, bits are typically numbered from right to left, starting with 0 (not 1). Each number denotes a **bit position**.

Given the bit sequence ``0000 0101``, the bits that are in position 0 and 2 have value 1, and the other bits have value 0.

Manipulating bits via std::bitset
**********************************

``std::bitset`` provides 4 key functions that are useful for doing bit manipulation:

* test() allows to query whether a bit is a 0 or 1
* set() allows to turn a bit on (this will do nothing if the bit is already on)
* reset() allows to turn a bit off (this will do nothing if the bit is already off)
* flip() allows to flip a bit value from a 0 to a 1 or vice versa

Each of these functions takes the position of the bit to operate on as their only argument.

Here's an example:

.. code-block:: cpp
    :linenos:

    std::bitset<8> bits{ 0b0000'0101 }; // we need 8 bits, start with bit pattern 0000 0101
    bits.set(3); // set bit position 3 to 1 (now we have 0000 1101)
    bits.flip(4); // flip bit 4 (now we have 0001 1101)
    bits.reset(4); // set bit 4 back to 0 (now we have 0000 1101)

``std::bitset`` doesn't allow getting or setting multiple bits at once. In order to do this, other methods should be used.
