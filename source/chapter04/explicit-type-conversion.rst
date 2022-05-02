###############################
Explicit type conversion
###############################

Introduction
***************

A way to convert any variable operands to another type in any given expression is needed.

C++ comes with a number of different **type casting operators** (more commonly called **casts**) that can be used by the programmer to request that the compiler perform a type conversion. Because casts are explicit requests by the programmer, this form of type conversion is often called an **explicit type conversion**.

Type casting
*************

C++ supports 5 different types of casts: **C-style casts**, **static casts**, **const casts**, **dynamic casts**, and **reinterpret casts**. The latter four are sometimes referred to as **named casts**.

**C-style casts** and **static casts** are being showed in this lesson.

C-style casts
***************

In standard C programming, casts are done via the ``()`` operator, with the name of the type to convert the value placed inside the parenthesis.

For example:

.. code-block:: cpp
    :linenos:

    int x { 10 };
    int y { 4 };
    double d { (double)x / y }; // convert x to a double so it becomes a floating point variable

C++ also allows using a C-style cast with a more function-call like syntax:

.. code-block:: cpp
    :linenos:

    int x { 10 };
    int y { 4 };
    double d { double(x) / y }; // convert x to a double so it becomes a floating point variable

This performs identically to the prior example, but has the benefit of parenthesizing the value being converted (making it easier to tell what is being converted).

Although a C-style cast appears to be a single cast, it can actually perform a variety of different conversions depending on context. This can include a static cast, a const cast or a reinterpret cast.

As a result, C-style casts are at risk for being inadvertently misused and not producing the expected behavior, something which is easily avoidable by using the C++ casts instead.

static_cast
*************

C++ introduces a casting operator called ``static_cast``, which can be used to convert a value of one type to a value of another type.

The ``static_cast`` operator takes an expression as input, and returns the evaluated value converted to the type specified inside the angled brackets. ``static_cast`` is best used to convert one fundamental type into another.

.. code-block:: cpp
    :linenos:

    int x { 10 };
    int y { 4 };
    double d { static_cast<double>(x) / y } // convert x to a double so it becomes a floating point variable

The main advantage of ``static_cast`` is that it provides compile-time type checking, making it harder to make an inadvertent error. ``static_cast`` is also (intentionally) less powerful than *C-style casts*, so developers can not inadvertently remove ``const`` or do other things you may not have intended to do.

Using static_cast to make narrowing conversions explicit
***********************************************************

Compilers will often issue warnings when a potentially unsafe (narrowing) implicit type conversion is performed. For example, consider the following program:

.. code-block:: cpp
    :linenos:

    int i { 48 };
    char ch = i; // implicit narrowing conversion

Casting an int to a char is potentially unsafe (as the compiler can't tell whether the integer value will overflow the range of the char or not), and so the compiler will typically print a warning or would yield an error.

.. code-block:: cpp
    :linenos:

    int i { 48 };
    // explicit conversion from int to char, so that a char is assigned to variable ch
    char ch { static_cast<char>(i) };

When ``static_cast`` is used, developers are explicitly telling the compiler that this conversion is intended, and they accept responsibility for the consequences (e.g. overflowing the range of a char if that happens).
