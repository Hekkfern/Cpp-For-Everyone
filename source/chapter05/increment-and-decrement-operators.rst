###################################
Increment and Decrement operators
###################################

Incrementing (adding 1 to) and decrementing (subtracting 1 from) a variable are both so common that they have their own operators.

+-------------------------------------+---------+---------+--------------------------------------------------+
| Operator                            | Symbol  | Form    | Operation                                        |
+=====================================+=========+=========+==================================================+
| Prefix increment (pre-increment)    | ``++``  | ``++x`` | Increment x, then return x                       |
+-------------------------------------+---------+---------+--------------------------------------------------+
| Prefix decrement (pre-decrement)    | ``--``  | ``--x`` | Decrement x, then return x                       |
+-------------------------------------+---------+---------+--------------------------------------------------+
| Postfix increment (post-increment)  | ``++``  | ``x++`` | Copy x, then increment x, then return the copy   |
+-------------------------------------+---------+---------+--------------------------------------------------+
| Postfix decrement (post-decrement)  | ``--``  | ``x--`` | Copy x, then decrement x, then return the copy   |
+-------------------------------------+---------+---------+--------------------------------------------------+

Note that there are two versions of each operator: a prefix version (where the operator comes before the operand) and a postfix version (where the operator comes after the operand).

On prefix increment/decrement operators, the operand is incremented or decremented first, and then expression evaluates to the value of the operand.

.. code-block:: cpp
    :linenos:

    int main()
    {
        int x { 5 };
        int y = ++x; // x is incremented to 6, x is evaluated to the value 6, and 6 is assigned to y

        std::cout << x << ' ' << y; // This prints "6 6"
        return 0;
    }

On postfix increment/decrement operators, a copy of the operand is made first. Then the operand (not the copy) is incremented or decremented. Finally, the copy (not the original) is evaluated.

.. code-block:: cpp
    :linenos:

    int main()
    {
        int x { 5 };
        int y = x++; // x is incremented to 6, copy of original x is evaluated to the value 5, and 5 is assigned to y

        std::cout << x << ' ' << y; // This prints "6 5"
        return 0;
    }

Note that the postfix version takes a lot more steps, and thus may not be as performant as the prefix version.
