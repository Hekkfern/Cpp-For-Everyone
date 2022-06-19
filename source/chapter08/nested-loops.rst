###############
Nested loops
###############

It is also possible to nest loops inside of other loops.

For each iteration of the outer loop, the body of the outer loop will execute once. Because the outer loop body contains an inner loop, the whole inner loop is executed for each iteration of the outer loop.

Inner loop can access variables from the outer loop, but not in the opposite direction.

An example of nested loops looks like this:

.. code-block:: cpp
    :linenos:

    int main()
    {
        // outer loops between 1 and 5
        int outer{ 1 };
        while (outer <= 5)
        {
            // For each iteration of the outer loop, the code in the body of the loop executes once

            // inner loops between 1 and outer
            int inner{ 1 };
            while (inner <= outer)
            {
                std::cout << inner << ' ';
                ++inner;
            }

            // print a newline at the end of each row
            std::cout << '\n';
            ++outer;
        }

        return 0;
    }

Like other types of loops, ``for loops`` can be nested inside other loops.

.. code-block:: cpp
    :linenos:

    int main()
    {
        for (char c{ 'a' }; c <= 'e'; ++c) // outer loop on letters
        {
            std::cout << c; // print our letter first

            for (int i{ 0 }; i < 3; ++i) // inner loop on all numbers
                std::cout << i;

            std::cout << '\n';
        }

        return 0;
    }
