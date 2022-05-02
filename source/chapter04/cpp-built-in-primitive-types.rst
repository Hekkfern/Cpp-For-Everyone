###################################################
4.1 C++ Built-in Primitive Types
###################################################

Bits, bytes, and memory addressing
***********************************

The smallest unit of memory is a **binary digit** (also called a **bit**), which can hold a value of 0 or 1.

Memory is organized into sequential units called **memory addresses** (or **addresses** for short). Similar to how a street address can be used to find a given house on a street, the memory address allows finding and accessing the contents of memory at a particular location.

Perhaps surprisingly, in modern computer architectures, each bit does not get its own unique memory address. This is because the number of memory addresses are limited, and the need to access data bit-by-bit is rare. Instead, each memory address holds one byte of data. A **byte** is a group of bits that are operated on as a unit. The modern standard is that a byte is comprised of 8 sequential bits.

Fundamental data types
***********************

C++ comes with built-in support for many different data types. These are called **fundamental data types**, but are often informally called **basic types**, **primitive types**, or **built-in types**.

+-----------------+-----------------------+---------------------------------------------------+----------+
| Types           | Category              | Meaning                                           | Example  |
+=================+=======================+===================================================+==========+
| float           | Floating Point        | a number with a fractional part                   | 3.14159  |
+-----------------+                       |                                                   |          |
| double          |                       |                                                   |          |
+-----------------+                       |                                                   |          |
| long double     |                       |                                                   |          |
+-----------------+-----------------------+---------------------------------------------------+----------+
| bool            | Integral (Boolean)    | true or false                                     | true     |
+-----------------+-----------------------+---------------------------------------------------+----------+
| char            | Integral (Character)  | a single character of text                        | 'c'      |
+-----------------+                       |                                                   |          |
| wchar_t         |                       |                                                   |          |
+-----------------+                       |                                                   |          |
| char8_t         |                       |                                                   |          |
+-----------------+                       |                                                   |          |
| char16_t        |                       |                                                   |          |
+-----------------+                       |                                                   |          |
| char32_t        |                       |                                                   |          |
+-----------------+-----------------------+---------------------------------------------------+----------+
| short           | Integral (Integer)    | positive and negative whole numbers, including 0  | 64       |
+-----------------+                       |                                                   |          |
| int             |                       |                                                   |          |
+-----------------+                       |                                                   |          |
| long            |                       |                                                   |          |
+-----------------+                       |                                                   |          |
| long long       |                       |                                                   |          |
+-----------------+-----------------------+---------------------------------------------------+----------+
| std::nullptr_t  | Null Pointer          | a null pointer                                    | nullptr  |
+-----------------+-----------------------+---------------------------------------------------+----------+
| void            | Void                  | not type                                          | n/a      |
+-----------------+-----------------------+---------------------------------------------------+----------+

An integer is a specific data type that hold non-fractional numbers, such as whole numbers, 0, and negative whole numbers.

Most modern programming languages include a fundamental string type (strings are a data type that lets us hold a sequence of characters, typically used to represent text). In C++, strings aren't a fundamental type (they are a compound type).

All of the integers (except int) can take an optional int suffix. However, this suffix should not be used. In addition to being more typing, adding the int suffix makes the type harder to distinguish from variables of type int. This can lead to mistakes if the short or long modifier is inadvertently missed.

.. code-block:: cpp

    short int si;
    long int li;
    long long int lli;

Variables can not be defined with a type of void.
