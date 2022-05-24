#############################
If statement
#############################

The most basic kind of conditional statement in C++ is the ``if statement``. An ``if statement`` takes the form:

.. code-block:: cpp
    :linenos:

    if (condition)
        true_statement;

or with an optional else statement:

.. code-block:: cpp
    :linenos:

    if (condition)
        true_statement;
    else
        false_statement;

If the ``condition`` evaluates to ``true``, the ``true_statement`` executes. If the ``condition`` evaluates to ``false`` and the optional ``else statement`` exists, the ``false_statement`` executes.

Here is a simple program that uses an ``if statement`` with the optional ``else statement``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << "Enter a number: ";
        int x{};
        std::cin >> x;

        if (x > 10)
            std::cout << x << " is greater than 10\n";
        else
            std::cout << x << " is not greater than 10\n";

        return 0;
    }

It's common to want to execute multiple statements based on some condition. To do so, a compound statement (block) can be used. Remember that blocks are treated as a single statement.

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << "Enter your height (in cm): ";
        int x{};
        std::cin >> x;

        if (x > 140)
            std::cout << "You are tall enough to ride.\n";
        else
        { // note addition of block here
            std::cout << "You are not tall enough to ride.\n";
            std::cout << "Too bad!\n";
        }

        return 0;
    }

If the programmer does not declare a block in the statement portion of an if statement or else statement, the compiler will implicitly declare one. Thus:

.. code-block:: cpp
    :linenos:

    if (condition)
        true_statement;
    else
        false_statement;

is actually the equivalent of:

.. code-block:: cpp
    :linenos:

    if (condition)
    {
        true_statement;
    }
    else
    {
        false_statement;
    }

It is possible to nest ``if statements`` within other ``if statements``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << "Enter a number: ";
        int x{};
        std::cin >> x;

        if (x >= 0) // outer if statement
            // it is bad coding style to nest if statements this way
            if (x <= 20) // inner if statement
                std::cout << x << " is between 0 and 20\n";

        return 0;
    }

Be careful with nesting ``if statements`` because an ``else statement`` is paired up with the last unmatched ``if statement`` in the same block. To avoid such ambiguities when nesting ``if statements``, it is a good idea to explicitly enclose the inner ``if statement`` within a block. This allows us to attach an else to either ``if statement`` without ambiguity.

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << "Enter a number: ";
        int x{};
        std::cin >> x;

        if (x >= 0)
        {
            if (x <= 20)
                std::cout << x << " is between 0 and 20\n";
            else // attached to inner if statement
                std::cout << x << " is greater than 20\n";
        }
        else // attached to outer if statement
            std::cout << x << " is negative\n";

        return 0;
    }

Nested ``if statements`` can be flattened by joining ``else``and ``if``keywords:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << "Enter a number: ";
        int x{};
        std::cin >> x;

        if (x < 0)
            std::cout << x << " is negative\n";
        else if (x <= 20) // only executes if x >= 0
            std::cout << x << " is between 0 and 20\n";
        else // only executes if x > 20
            std::cout << x << " is greater than 20\n";

        return 0;
    }

Logical operators to check multiple conditions within a single ``if statement``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << "Enter an integer: ";
        int x{};
        std::cin >> x;

        std::cout << "Enter another integer: ";
        int y{};
        std::cin >> y;

        if (x > 0 && y > 0) // && is logical and -- checks if both conditions are true
            std::cout << "Both numbers are positive\n";
        else if (x > 0 || y > 0) // || is logical or -- checks if either condition is true
            std::cout << "One of the numbers is positive\n";
        else
            std::cout << "Neither number is positive\n";

        return 0;
    }
