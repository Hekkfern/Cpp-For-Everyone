###############################
Standard conversions
###############################

Introduction
*************************

The C++ language standard defines how different fundamental types (and in some cases, compound types) can be converted to other types. These conversion rules are called the **standard conversions**.

The standard conversions can be broadly divided into 4 categories, each covering different types of conversions:

* Numeric promotions
* Numeric conversions
* Arithmetic conversions
* Other conversions (which includes various pointer and reference conversions)

When a type conversion is needed, the compiler will see if there are standard conversions that it can use to convert the value to the desired type. The compiler may apply zero, one, or more than one standard conversions in the conversion process.

Numeric promotions
********************

A **numeric promotion** is the type conversion of a narrower numeric type (such as a char) to a wider numeric type (typically int or double) that can be processed efficiently and is less likely to have a result that overflows.

All numeric promotions are **value-preserving**, which means that all values in the original type are representable without loss of data or precision in the new type. Because such promotions are safe, the compiler will freely use numeric promotion as needed, and will not issue a warning when doing so.

The numeric promotion rules are divided into two subcategories: integral promotions and floating point promotions.

Floating point promotions
==========================

Using the floating point promotion rules, a value of type ``float`` can be converted to a value of type ``double``.

.. code-block:: cpp

    void printDouble(double d)
    {
        std::cout << d;
    }
    int main()
    {
        printDouble(5.0); // no conversion necessary
        printDouble(4.0f); // numeric promotion of float to double

        return 0;
    }

Integral promotions
====================

Using the integral promotion rules, the following conversions can be made:

* ``signed char`` or ``signed short`` can be converted to ``int``.
* ``unsigned char``, ``char8_t``, and ``unsigned short`` can be converted to int if int can hold the entire range of the type, or ``unsigned int`` otherwise.
* If ``char`` is signed by default, it follows the ``signed char`` conversion rules above. If it is unsigned by default, it follows the ``unsigned char`` conversion rules above.
* ``bool`` can be converted to ``int``, with ``false`` becoming ``0`` and ``true`` becoming ``1``.

There are a few other integral promotion rules that are used less often. These can be found at `cppreference <https://en.cppreference.com/w/cpp/language/implicit_conversion#Integral_promotion>`_.

Numeric conversions
*********************

Some value-preserving type conversions (such as ``char`` to ``short``, ``int`` to ``long``, or ``int`` to ``double``) are not considered to be numeric promotions in C++ (they are numeric conversions). This is because such conversions do not assist in the goal of converting smaller types to larger types that can be processed more efficiently.

The distinction is mostly academic. However, in certain cases, the compiler will favor numeric promotions over numeric conversions.

There are five basic types of numeric conversions:

* Converting an integral type to any other integral type (excluding integral promotions):

.. code-block:: cpp

    short s = 3; // convert int to short
    long l = 3; // convert int to long
    char ch = s; // convert short to char

* Converting a floating point type to any other floating point type (excluding floating point promotions):

.. code-block:: cpp

    float f = 3.0; // convert double to float
    long double ld = 3.0; // convert double to long double

* Converting a floating point type to any integral type:

.. code-block:: cpp

    int i = 3.5; // convert double to int

* Converting an integral type to any floating point type:

.. code-block:: cpp

    double d = 3; // convert int to double

* Converting an integral type or a floating point type to a bool:

.. code-block:: cpp

    bool b1 = 3; // convert int to bool
    bool b2 = 3.0; // convert double to bool


Unlike a numeric promotion (which is always safe), a numeric conversion may (or may not) result in the loss of data or precision.

Some numeric conversions are always safe (such as int to long, or int to double). Other numeric conversions, such as double to int, may result in the loss of data (depending on the specific value being converted and/or the range of the underlying types):abbr:

.. code-block:: cpp

    int i1 = 3.5; // the 0.5 is dropped, resulting in lost data
    int i2 = 3.0; // okay, will be converted to value 3, so no data is lost

In C++, a narrowing conversion is a numeric conversion that may result in the loss of data. Such narrowing conversions include:

* From a floating point type to an integral type.
* From a wider floating point type to a narrower floating point type, unless the value being converted is ``constexpr`` and is in range of the destination type (even if the narrower type doesn't have the precision to store the whole number).
* From an integral to a floating point type, unless the value being converted is ``constexpr`` and is in range of the destination type and can be converted back into the original type without data loss.
* From a wider integral type to a narrower integral type, unless the value being converted is ``constexpr`` and after integral promotion will fit into the destination type.

Narrowing conversions are strictly disallowed when using brace initialization (which is one of the primary reasons this initialization form is preferred).

Arithmetic conversions
***********************

In C++, certain operators require that their operands be of the same type. If one of these operators is invoked with operands of different types, one or both of the operands will be implicitly converted to matching types using a set of rules called the **usual arithmetic conversions**.

The following operators require their operands to be of the same type:

* The binary arithmetic operators: ``+``, ``-``, ``*``, ``/``, ``%``
* The binary relational operators: ``<``, ``>``, ``<=``, ``>=``, ``==``, ``!=``
* The binary bitwise arithmetic operators: ``&``, ``^``, ``|``
* The conditional operator ``?:`` (excluding the condition, which is expected to be of type ``bool``)

The usual arithmetic conversion rules are pretty simple. The compiler has a prioritized list of types that looks something like this:

* long double (highest)
* double
* float
* unsigned long long
* long long
* unsigned long
* long
* unsigned int
* int (lowest)

There are only two rules:

* If the type of at least one of the operands is on the priority list, the operand with lower priority is converted to the type of the operand with higher priority.
* Otherwise (the type of neither operand is on the list), both operands are numerically promoted (see :ref:`chapter04/standard-conversions:Numeric promotions`).
