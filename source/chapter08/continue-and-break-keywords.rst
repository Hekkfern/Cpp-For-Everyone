#############################
continue and break keywords
#############################

Break statement
****************

The **break statement** causes a while loop, do-while loop, for loop, or switch statement to end, with execution continuing with the next statement after the loop or switch being broken out of.

In the context of a ``switch statement``, a ``break`` is typically used at the end of each case to signify the case is finished (which prevents fallthrough into subsequent cases):

For example:

.. code-block:: cpp
    :linenos:

    void printMath(int x, int y, char ch)
    {
        switch (ch)
        {
        case '+':
            std::cout << x << " + " << y << " = " << x + y << '\n';
            break; // don't fall-through to next case
        case '-':
            std::cout << x << " - " << y << " = " << x - y << '\n';
            break; // don't fall-through to next case
        case '*':
            std::cout << x << " * " << y << " = " << x * y << '\n';
            break; // don't fall-through to next case
        case '/':
            std::cout << x << " / " << y << " = " << x / y << '\n';
            break;
        }
    }

    int main()
    {
        printMath(2, 3, '+');

        return 0;
    }

In the context of a loop, a ``break`` statement can be used to end the loop early. Execution continues with the next statement after the end of the loop.

For example:

.. code-block:: cpp
    :linenos:

    int main()
    {
        int sum{ 0 };

        // Allow the user to enter up to 10 numbers
        for (int count{ 0 }; count < 10; ++count)
        {
            std::cout << "Enter a number to add, or 0 to exit: ";
            int num{};
            std::cin >> num;

            // exit loop if user enters 0
            if (num == 0)
                break; // exit the loop now

            // otherwise add number to our sum
            sum += num;
        }

        // execution will continue here after the break
        std::cout << "The sum of all the numbers you entered is: " << sum << '\n';

        return 0;
    }

Break is also a common way to get out of an intentional infinite loop:

.. code-block:: cpp
    :linenos:

    int main()
    {
        while (true) // infinite loop
        {
            std::cout << "Enter 0 to exit or any other integer to continue: ";
            int num{};
            std::cin >> num;

            // exit loop if user enters 0
            if (num == 0)
                break;
        }

        std::cout << "We're out!\n";

        return 0;
    }

continue statement
*******************

The **continue statement** provides a convenient way to end the current iteration of a loop without terminating the entire loop.

Here's an example of using ``continue``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        for (int count{ 0 }; count < 10; ++count)
        {
            // if the number is divisible by 4, skip this iteration
            if ((count % 4) == 0)
                continue; // go to next iteration

            // If the number is not divisible by 4, keep going
            std::cout << count << '\n';

            // The continue statement jumps to here
        }

        return 0;
    }

``Continue statements`` work by causing the current point of execution to jump to the bottom of the current loop.

In the case of a for loop, the ``end-statement`` of the for loop still executes after a ``continue`` (since this happens after the end of the loop body).
