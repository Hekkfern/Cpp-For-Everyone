###################################################
Floating point numbers
###################################################

Introduction
****************

A floating point type variable is a variable that can hold a real number, such as ``4320.0``, ``-3.33``, or ``0.01226``. The floating part of the name floating point refers to the fact that the decimal point can “float”; that is, it can support a variable number of digits before and after the decimal point.

There are three different floating point data types: float, double, and long double. As with integers, C++ does not define the actual size of these types (but it does guarantee minimum sizes). On modern architectures, floating point representation almost always follows **IEEE 754** binary format.

Floating point data types are always signed (can hold positive and negative values).

+--------------+---------------+--------------------+
| Type         | Minimum Size  | Typical Size       |
+==============+===============+====================+
| float        | 4 bytes       | 4 bytes            |
+--------------+---------------+--------------------+
| double       | 8 bytes       | 8 bytes            |
+--------------+---------------+--------------------+
| long double  | 8 bytes       | 8, 12 or 16 bytes  |
+--------------+---------------+--------------------+

Here are some definitions of floating point numbers:

.. code-block:: cpp
    :linenos:

    float fValue;
    double dValue;
    long double ldValue;

When using floating point literals, always at least one decimal place must be included (even if the decimal is 0). This helps the compiler understand that the number is a floating point number and not an integer.

.. code-block:: cpp
    :linenos:

    int x{5}; // 5 means integer
    double y{5.0}; // 5.0 is a floating point literal (no suffix means double type by default)
    float z{5.0f}; // 5.0 is a floating point literal, f suffix means float type

Note that by default, floating point literals default to type double.

Floating point range
*********************

Assuming **IEEE 754** representation:

+------------------------------------------+-------------------------------------------------------------------+------------------------------------------+
| Size                                     | Range                                                             | Precision                                |
+==========================================+===================================================================+==========================================+
| 4 bytes                                  | :math:`\pm1.18\cdot 10^{-38}` to :math:`\pm3.4\cdot 10^{38}`      | 6-9 significant digits, typically 7      |
+------------------------------------------+-------------------------------------------------------------------+------------------------------------------+
| 8 bytes                                  | :math:`\pm2.23\cdot 10^{-308}` to :math:`\pm1.80\cdot 10^{308}`   | 15-18 significant digits, typically 16   |
+------------------------------------------+-------------------------------------------------------------------+------------------------------------------+
| 80-bits (typically uses 12 or 16 bytes)  | :math:`\pm3.36\cdot 10^{-4932}` to :math:`\pm1.18\cdot 10^{4932}` | 18-21 significant digits                 |
+------------------------------------------+-------------------------------------------------------------------+------------------------------------------+
| 16 bytes                                 | :math:`\pm3.36\cdot 10^{-4932}` to :math:`\pm1.18\cdot 10^{4932}` | 33-36 significant digits                 |
+------------------------------------------+-------------------------------------------------------------------+------------------------------------------+

The 80-bit floating point type is a bit of a historical anomaly. On modern processors, it is typically implemented using 12 or 16 bytes (which is a more natural size for processors to handle).

It may seem a little odd that the 80-bit floating point type has the same range as the 16-byte floating point type. This is because they have the same number of bits dedicated to the exponent. However, the 16-byte number can store more significant digits.

Floating point precision
****************************

On a computer, an infinite length number would require infinite memory to store, and typically variables only have 4 or 8 bytes. This limited memory means floating point numbers can only store a certain number of significant digits, and any additional significant digits are lost. The number that is actually stored will be close to the desired number, but not exact.

The precision of a floating point number defines how many significant digits it can represent without information loss.

The number of digits of precision a floating point variable has depends on both the size (floats have less precision than doubles) and the particular value being stored (some values have more precision than others).

Rounding errors occur when a number can't be stored precisely. This can happen even with simple numbers, like ``0.1``. Therefore, rounding errors can, and do, happen all the time. Rounding errors aren't the exception; they're the rule. Developers must not assume that floating point numbers are exact.

Mathematical operations (such as addition and multiplication) tend to make rounding errors grow.

Floating point comparisons
****************************

Rounding errors due to lack of precision may make a number either slightly smaller or slightly larger, depending on where the truncation happens.

Because floating point numbers tend to be inexact, comparing floating point numbers is generally problematic. This operation can not be done as easily as integer values does.
