#############################
Infinite loops
#############################

If the expression of a loop always evaluates to ``true``, the loop will execute forever. This is called an **infinite loop**.

Here is an example of an infinite loop using the ``while statement``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        int count{ 1 };
        while (count <= 10) // this condition will never be false
        {
            std::cout << count << ' '; // so this line will repeatedly execute
        }

        return 0; // this line will never execute
    }

Some infinite loop are errors because the developer forgot to add an statement to update the loop variable.

However, it is desired sometimes to create an infinite loop to make the program execution to stay trapped in there for a while.

An intentional infinite loop can be declared like this:

.. code-block:: cpp
    :linenos:

    while (true)
    {
        // this loop will execute forever
    }

The only way to exit an infinite loop is through a ``return statement``, a ``break statement``, an ``exit statement``, a ``goto statement``, an exception being thrown, or the user killing the program.

Note that if all the statements and expressions of a ``for loop`` are omitted, an infinite loop is created too:

.. code-block:: cpp
    :linenos:

    for (;;)
        statement;
