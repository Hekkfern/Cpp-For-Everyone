###################################################
4.4 Fixed-width integers and size_t
###################################################

Why isn't the size of the integer variables fixed?
***************************************************

This goes back to C, when computers were slow and performance was of the utmost concern. C opted to intentionally leave the size of an integer open so that the compiler implementers could pick a size for int that performs best on the target computer architecture.

Fixed-width integers
************************

To address the above issues, C99 defined a set of **fixed-width integers** (in the ``stdint.h`` header) that are guaranteed to be the same size on any architecture.

These are defined as follows:

+----------------+------------------+-----------------------------------------------------------+
| Name           | Type             | Range                                                     |
+================+==================+===========================================================+
| std::int8_t    | 1 byte signed    | -128 to 127                                               |
+----------------+------------------+-----------------------------------------------------------+
| std::uint8_t   | 1 byte unsigned  | 0 to 255                                                  |
+----------------+------------------+-----------------------------------------------------------+
| std::int16_t   | 2 byte signed    | -32,768 to 32,767                                         |
+----------------+------------------+-----------------------------------------------------------+
| std::uint16_t  | 2 byte unsigned  | 0 to 65,535                                               |
+----------------+------------------+-----------------------------------------------------------+
| std::int32_t   | 4 byte signed    | -2,147,483,648 to 2,147,483,647                           |
+----------------+------------------+-----------------------------------------------------------+
| std::uint32_t  | 4 byte unsigned  | 0 to 4,294,967,295                                        |
+----------------+------------------+-----------------------------------------------------------+
| std::int64_t   | 8 byte signed    | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807   |
+----------------+------------------+-----------------------------------------------------------+
| std::uint64_t  | 8 byte unsigned  | 0 to 18,446,744,073,709,551,615                           |
+----------------+------------------+-----------------------------------------------------------+

C++ officially adopted these fixed-width integers as part of C++11. They can be accessed by including the ``<cstdint>`` header, where they are defined inside the std namespace.

The fixed-width integers have two downsides:

* The fixed-width integers are not guaranteed to be defined on all architectures. They only exist on systems where there are fundamental types matching their widths and following a certain binary representation. However, given that most modern architectures have standardized around 8/16/32/64-bit variables, this is unlikely to be a problem.
* It may be slower than a wider type on some architectures. For example, if an 32-bits integer is needed, a smart decision would be to use std::int32_t, but the CPU might actually be faster at processing 64-bit integers. However, just because your CPU can process a given type faster does not mean the program will be faster overall.

Fast and least integers
**************************

To help address the above downsides, C++ also defines two alternative sets of integers that are guaranteed to be defined.

The fast types (``std::int_fast#_t`` and ``std::uint_fast#_t``) provide the fastest signed/unsigned integer type with a width of at least # bits (where # = 8, 16, 32, or 64). For example, ``std::int_fast32_t`` is the fastest signed integer type that is at least 32 bits.

The least types (``std::int_least#_t`` and ``std::uint_least#_t``) provide the smallest signed/unsigned integer type with a width of at least # bits (where # = 8, 16, 32, or 64). For example, ``std::uint_least32_t`` is the smallest unsigned integer type that is at least 32 bits.

However, these fast and least integers have their own downsides:

* Not many programmers actually use them, and a lack of familiarity can lead to errors.
* The fast types can lead to some memory wastage because the bit numbers can be greater than it is needed to store the expected values. Most seriously, because the size of the fast/least integers can vary, it is possible that the program may exhibit different behaviors on architectures where they resolve to different sizes.

What is std::size_t?
***********************

``sizeof()`` function (and many functions that return a size or length value) return a value of type ``std::size_t``. ``std::size_t`` is defined as an unsigned integral type, and it is typically used to represent the size or length of objects.

Much like an integer can vary in size depending on the system, ``std::size_t`` also varies in size. ``std::size_t`` is guaranteed to be unsigned and at least 16 bits, but on most systems will be equivalent to the address-width of the application. That is, for 32-bit applications, ``std::size_t`` will typically be a 32-bit unsigned integer, and for a 64-bit application, size_t will typically be a 64-bit unsigned integer. size_t is defined to be big enough to hold the size of the largest object creatable on your system (in bytes).
