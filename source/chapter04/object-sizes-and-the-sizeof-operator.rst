###################################################
4.3 Object sizes and the sizeof operator
###################################################

Object sizes
***********************************

Because memory is typically accessed through variable names (and not directly via memory addresses), the compiler is able to hide the details of how many bytes a given object uses. When some variable ``x`` is accessed, the compiler knows how many bytes of data to retrieve (based on the type of variable ``x``), and can handle that task on its own.

Even so, there are several reasons it is useful to know how much memory an object uses.

First, the more memory an object uses, the more information it can hold. For example, a single bit can hold 2 possible values, a 0, or a 1; but 3 bits can hold 8 possible values.

To generalize, an object with n bits (where n is an integer) can hold :math:`2^{n}` (2 to the power of n) unique values.

Thus, the size of the object puts a limit on the amount of unique values it can store. Objects that utilize more bytes can store a larger number of unique values.

Second, computers have a finite amount of free memory. Every time an object is defined, a small portion of that free memory is used for as long as the object is in existence. Because modern computers have a lot of memory, this impact is usually negligible. However, for programs that need a large amount of objects or data, the difference between using 1 byte and 8 byte objects can be significant.

Fundamental data type sizes
***********************************

The size of a given data type is dependent on the compiler and/or the computer architecture

C++ only guarantees that each fundamental data types will have a minimum size.

+-----------------+--------------+---------------+-------------------------+
| Category        | Type         | Minimum Size  | Note                    |
+=================+==============+===============+=========================+
| boolean         | bool         | 1 byte        |                         |
+-----------------+--------------+---------------+-------------------------+
| character       | char         | 1 byte        | Always exactly 1 byte   |
+                 +--------------+---------------+-------------------------+
|                 | wchar_t      | 1 byte        |                         |
+                 +--------------+---------------+-------------------------+
|                 | char16_t     | 2 bytes       |                         |
+                 +--------------+---------------+-------------------------+
|                 | char32_t     | 4 bytes       |                         |
+-----------------+--------------+---------------+-------------------------+
| integer         | short        | 2 bytes       |                         |
+                 +--------------+---------------+-------------------------+
|                 | int          | 2 bytes       |                         |
+                 +--------------+---------------+-------------------------+
|                 | long         | 4 bytes       |                         |
+-----------------+--------------+---------------+-------------------------+
| floating point  | long long    | 8 bytes       |                         |
+                 +--------------+---------------+-------------------------+
|                 | float        | 4 bytes       |                         |
+                 +--------------+---------------+-------------------------+
|                 | double       | 8 bytes       |                         |
+                 +--------------+---------------+-------------------------+
|                 | long double  | 8 bytes       |                         |
+-----------------+--------------+---------------+-------------------------+

However, the actual size of the variables may be different on your machine (particularly int, which is more often 4 bytes).

For maximum compatibility, it should not be assumed that variables are larger than the specified minimum size.

The sizeof operator
*********************

In order to determine the size of data types on a particular machine, C++ provides an operator named ``sizeof``. The **sizeof operator** is a unary operator that takes either a type or a variable, and returns its size in bytes.
