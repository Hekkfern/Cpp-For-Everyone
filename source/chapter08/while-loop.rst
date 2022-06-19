#############################
While loop
#############################

The **while statement** (also called a **while loop**) is the simplest of the three loop types that C++ provides, and it has a definition very similar to that of an ``if statement``:

.. code-block:: cpp
    :linenos:

    while (condition)
        statement;

A ``while statement`` is declared using the **while** keyword. When a ``while statement`` is executed, the ``condition`` is evaluated. If the condition evaluates to ``true``, the associated statement executes.

However, unlike an ``if statement``, once the statement has finished executing, control returns to the top of the ``while statement`` and the process is repeated. This means a ``while statement`` will keep looping for as long as the condition evaluates to ``true``.

This simple while loop shows how to print all the numbers from 1 to 10:

.. code-block:: cpp
    :linenos:

    int main()
    {
        int count{ 1 };
        while (count <= 10)
        {
            std::cout << count << ' ';
            ++count;
        }

        std::cout << "done!";

        return 0;
    }
