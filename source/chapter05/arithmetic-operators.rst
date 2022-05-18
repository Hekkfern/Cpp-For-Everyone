######################
Arithmetic operators
######################

Unary arithmetic operators
***************************

**Unary operators** are operators that only take one operand.

There are two unary arithmetic operators, plus (+), and minus (-):

+-------------+---------+--------+----------------+
| Operator    | Symbol  | Form   | Operation      |
+=============+=========+========+================+
| Unary plus  | ``+``   | ``+x`` | Value of x     |
+-------------+---------+--------+----------------+
| Unary minus | ``-``   | ``-x`` | Negation of x  |
+-------------+---------+--------+----------------+

The **unary minus** operator returns the operand multiplied by ``-1``. In other words, if ``x = 5``, ``-x`` is ``-5``.

The **unary plus** operator returns the value of the operand. In other words, ``+5`` is ``5``, and ``+x`` is ``x``. Generally this operator is not used since it's redundant. It was added largely to provide symmetry with the unary minus operator.

For best effect, both of these operators should be placed immediately preceding the operand (e.g. ``-x``, not ``- x``).

Binary arithmetic operators
****************************

**Binary operators** are operators that take a left and right operand.

There are 5 binary arithmetic operators:

+----------------------+---------+-----------+----------------------------------+
| Operator             | Symbol  | Form      | Operation                        |
+======================+=========+===========+==================================+
| Addition             | ``+``   | ``x + y`` | x plus y                         |
+----------------------+---------+-----------+----------------------------------+
| Subtraction          | ``-``   | ``x - y`` | x minus y                        |
+----------------------+---------+-----------+----------------------------------+
| Multiplication       | ``*``   | ``x * y`` | x multiplied by y                |
+----------------------+---------+-----------+----------------------------------+
| Division             | ``/``   | ``x / y`` | x divided by y                   |
+----------------------+---------+-----------+----------------------------------+
| Modulus (Remainder)  | ``%``   | ``x % y`` | The remainder of x divided by y  |
+----------------------+---------+-----------+----------------------------------+

Integer and floating point division
************************************

Division and modulus (remainder) need some additional explanation, because they don't work as they do in real life.

If either (or both) of the operands are floating point values, the *division operator* performs floating point division. **Floating point division** returns a floating point value, and the fraction is kept. For example, ``7.0 / 4 = 1.75``, ``7 / 4.0 = 1.75``, and ``7.0 / 4.0 = 1.75``. As with all floating point arithmetic operations, rounding errors may occur.

If both of the operands are integers, the *division operator* performs integer division instead. **Integer division** drops any fractions and returns an integer value. For example, ``7 / 4 = 1`` because the fractional portion of the result is dropped. Similarly, ``-7 / 4 = -1`` because the fraction is dropped.

So, what if there are two integers, and is it desired to divide them without losing the fraction? ``static_cast<>`` can be used to convert an integer to a floating point number so that floating point division is executed instead of integer division.

For example:

.. code-block:: cpp
    :linenos:

    int main()
    {
        int x{ 7 };
        int y{ 4 };

        std::cout << "int / int = " << x / y << '\n';
        std::cout << "double / int = " << static_cast<double>(x) / y << '\n';
        std::cout << "int / double = " << x / static_cast<double>(y) << '\n';
        std::cout << "double / double = " << static_cast<double>(x) / static_cast<double>(y) << '\n';

        return 0;
    }

This produces the result:

.. code-block:: none

    int / int = 1
    double / int = 1.75
    int / double = 1.75
    double / double = 1.75

The above illustrates that if either operand is a floating point number, the result will be floating point division, not integer division.

Dividing by zero
*****************

Trying to divide by ``0`` (or ``0.0``) will generally cause the program to crash, as the results are mathematically undefined!

The modulus operator
*********************

The **modulus operator** (also informally known as the *remainder operator*) is an operator that returns the remainder after doing an integer division. For example, 7 / 4 = 1 remainder 3. Therefore, ``7 % 4 = 3``.

Modulus only works with integer operands.

Modulus is most useful for testing whether a number is evenly divisible by another number (meaning that after division, there is no remainder): if ``x % y`` evaluates to ``0``, then we know that ``x`` is evenly divisible by ``y``.

The modulus operator can also work with negative operands. ``x % y`` always returns results with the sign of ``x``.

Arithmetic assignment operators
*******************************

+----------------------------+---------+------------+-------------------------------------+
| Operator                   | Symbol  | Form       | Operation                           |
+============================+=========+============+=====================================+
| Assignment                 | ``=``   | ``x = y``  | Assign value y to x                 |
+----------------------------+---------+------------+-------------------------------------+
| Addition assignment        | ``+=``  | ``x += y`` | Add y to x                          |
+----------------------------+---------+------------+-------------------------------------+
| Subtraction assignment     | ``-=``  | ``x -= y`` | Subtract y from x                   |
+----------------------------+---------+------------+-------------------------------------+
| Multiplication assignment  | ``*=``  | ``x *= y`` | Multiply x by y                     |
+----------------------------+---------+------------+-------------------------------------+
| Division assignment        | ``/=``  | ``x /= y`` | Divide x by y                       |
+----------------------------+---------+------------+-------------------------------------+
| Modulus assignment         | ``%=``  | ``x %= y`` | Put the remainder of ``x / y`` in x |
+----------------------------+---------+------------+-------------------------------------+

Because writing statements such as ``x = x + 4`` is so common, C++ provides five arithmetic assignment operators for convenience. Instead of writing ``x = x + 4``, ``x += 4`` can be written alternatively. Or, instead of ``x = x * y``, ``x *= y`` can be written.

Where's the exponent operator?
*******************************

C++ does not include an exponent operator.

Note that the ``^`` operator (commonly used to denote exponentiation in mathematics) is a *Bitwise XOR* operation in C++.

To do exponents in C++, #include the <cmath> header, and use the pow() function:

.. code-block:: cpp
    :linenos:

    #include <cmath>

    double x{ std::pow(3.0, 4.0) }; // 3 to the 4th power

Note that the parameters (and return value) of function ``pow()`` are of type double. Due to rounding errors in floating point numbers, the results of ``pow()`` may not be precise.
