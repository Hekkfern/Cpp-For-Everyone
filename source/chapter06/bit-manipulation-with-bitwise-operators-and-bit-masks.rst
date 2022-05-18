#########################################################
Bit manipulation with bitwise operators and bit masks
#########################################################

This chapter will show how bitwise operators are more commonly used.

Bit masks
**********

In order to manipulate individual bits (e.g. turn them on or off), some way to identify the specific bits to manipulate is required. Unfortunately, the bitwise operators don't know how to work with bit positions. Instead they work with bit masks.

A **bit mask** is a predefined set of bits that is used to select which specific bits will be modified by subsequent operations. The bit mask blocks the bitwise operators from touching undesired bits, and allows access to the ones to be modified.

The simplest set of bit masks is to define one bit mask for each bit position. 0s are used to mask out the undesired bits, and 1s to denote the bits to modify.

Although bit masks can be literals, they're often defined as symbolic constants so they can be given a meaningful name and easily reused.

.. code-block:: cpp
    :linenos:

    constexpr std::uint8_t mask0{ 0b0000'0001 }; // represents bit 0
    constexpr std::uint8_t mask1{ 0b0000'0010 }; // represents bit 1
    constexpr std::uint8_t mask2{ 0b0000'0100 }; // represents bit 2
    constexpr std::uint8_t mask3{ 0b0000'1000 }; // represents bit 3
    constexpr std::uint8_t mask4{ 0b0001'0000 }; // represents bit 4
    constexpr std::uint8_t mask5{ 0b0010'0000 }; // represents bit 5
    constexpr std::uint8_t mask6{ 0b0100'0000 }; // represents bit 6
    constexpr std::uint8_t mask7{ 0b1000'0000 }; // represents bit 7

Testing a bit (to see if it is on or off)
******************************************

Bit masks can be used in conjunction with a bit flag variable to manipulate other bit flags.

To determine if a bit is on or off, *bitwise AND* is used in conjunction with the bit mask for the appropriate bit.

.. code-block:: cpp
    :linenos:

    std::uint8_t flags{ 0b0000'0101 }; // 8 bits in size means room for 8 flags

	std::cout << "bit 0 is " << ((flags & mask0) ? "on\n" : "off\n"); // prints "bit 0 is on"
	std::cout << "bit 1 is " << ((flags & mask1) ? "on\n" : "off\n"); // prints "bit 1 is off"

Setting a bit
**************

To set (turn on) a bit, *bitwise OR equals* (operator ``|=``) is used in conjunction with the bit mask for the appropriate bit:

.. code-block:: cpp
    :linenos:

    std::uint8_t flags{ 0b0000'0101 }; // 8 bits in size means room for 8 flags

    std::cout << "bit 1 is " << ((flags & mask1) ? "on\n" : "off\n"); // prints bit 1 is off

    flags |= mask1; // turn on bit 1

    std::cout << "bit 1 is " << ((flags & mask1) ? "on\n" : "off\n"); // prints "bit 1 is on"


Turning on multiple bits at the same time using *Bitwise OR* is possible:

.. code-block:: cpp

    flags |= (mask4 | mask5); // turn bits 4 and 5 on at the same time

Resetting a bit
****************

To clear a bit (turn off), *Bitwise AND* and *Bitwise NOT* are used together:

.. code-block:: cpp
    :linenos:

    std::uint8_t flags{ 0b0000'0101 }; // 8 bits in size means room for 8 flags

    std::cout << "bit 2 is " << ((flags & mask2) ? "on\n" : "off\n"); // prints "bit 2 is on"

    flags &= ~mask2; // turn off bit 2

    std::cout << "bit 2 is " << ((flags & mask2) ? "on\n" : "off\n"); // prints "bit 2 is off"

Turning off multiple bits at the same time is also possible:

.. code-block:: cpp

    flags &= ~(mask4 | mask5); // turn bits 4 and 5 off at the same time

Flipping a bit
****************

To toggle a bit state, *Bitwise XOR* is used:

.. code-block:: cpp
    :linenos:

    std::uint8_t flags{ 0b0000'0101 }; // 8 bits in size means room for 8 flags

    std::cout << "bit 2 is " << ((flags & mask2) ? "on\n" : "off\n"); // prints "bit 2 is on"
    flags ^= mask2; // flip bit 2
    std::cout << "bit 2 is " << ((flags & mask2) ? "on\n" : "off\n"); // prints "bit 2 is off"
    flags ^= mask2; // flip bit 2
    std::cout << "bit 2 is " << ((flags & mask2) ? "on\n" : "off\n"); // prints "bit 2 is on"

It is possible to flip multiple bits simultaneously:

.. code-block:: cpp

    flags ^= (mask4 | mask5); // flip bits 4 and 5 at the same time

Bit masks and std::bitset
***************************

``std::bitset`` supports the full set of bitwise operators. So even though it's easier to use the functions (test, set, reset, and flip) to modify individual bits, using bitwise operators and bit masks is also possible.

The bitwise operators allow you to modify multiple bits at once, unlike ``std::bitset``.
