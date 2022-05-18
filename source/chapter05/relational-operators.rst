######################
Relational operators
######################

**Relational operators** are operators that let you compare two values. There are 6 relational operators:

+-------------------------+---------+------------+------------------------------------------------------------+
| Operator                | Symbol  | Form       | Operation                                                  |
+=========================+=========+============+============================================================+
| Greater than            | ``>``   | ``x > y``  | true if x is greater than y, false otherwise               |
+-------------------------+---------+------------+------------------------------------------------------------+
| Less than               | ``<``   | ``x < y``  | true if x is less than y, false otherwise                  |
+-------------------------+---------+------------+------------------------------------------------------------+
| Greater than or equals  | ``>=``  | ``x >= y`` | true if x is greater than or equal to y, false otherwise   |
+-------------------------+---------+------------+------------------------------------------------------------+
| Less than or equals     | ``<=``  | ``x <= y`` | true if x is less than or equal to y, false otherwise      |
+-------------------------+---------+------------+------------------------------------------------------------+
| Equality                | ``==``  | ``x == y`` | true if x equals y, false otherwise                        |
+-------------------------+---------+------------+------------------------------------------------------------+
| Inequality              | ``!=``  | ``x != y`` | true if x does not equal y, false otherwise                |
+-------------------------+---------+------------+------------------------------------------------------------+

Each of these operators evaluates to the boolean value true (1), or false (0).

Boolean conditional values
***************************

By default, conditions in an if statement or conditional operator (and a few other places) evaluate as Boolean values.

Statements like ``if (b1 == true) ...`` are redundant, as the ``== true`` doesn't actually add any value to the condition. Instead, ``if (b1) ...`` should be used. Similarly, the following ``if (b1 == false) ...`` is better written as ``if (!b1) ...``.

Comparison of floating point values can be problematic
********************************************************

If a high level of precision is required, comparing floating point values using any of the relational operators can be dangerous. This is because floating point values are not precise, and small rounding errors in the floating point operands may cause unexpected results.

When the less than and greater than operators (``<``, ``<=``, ``>``, and ``>=``) are used with floating point values, they will usually produce the correct answer (only potentially failing when the operands are almost identical). Because of this, use of these operators with floating point operands can be acceptable, so long as the consequence of getting a wrong answer when the operands are similar is slight.

The equality operators (``==`` and ``!=``) are much more troublesome. Consider operator==, which returns true only if its operands are exactly equal. Because even the smallest rounding error will cause two floating point numbers to not be equal, operator== is at high risk for returning false when a true might be expected.

Operator ``!=`` has the same kind of problem.

So how can two floating point operands be compared to see if they are equal?

The most common method of doing floating point equality involves using a function that looks to see if two numbers are almost the same. If they are “close enough”, then we call them equal. The value used to represent “close enough” is traditionally called **epsilon**. Epsilon is generally defined as a small positive number (e.g. ``0.00000001``, sometimes written ``1e-8``).

However, an epsilon that's appropriate for the operands must be chosen every time.

Comparison of floating point numbers is a difficult topic, and there's no “one size fits all” algorithm that works for every case.
