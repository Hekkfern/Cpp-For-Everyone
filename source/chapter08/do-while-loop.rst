#############################
Do-while loop
#############################

A ``while loop`` evaluates the condition up front. But there is another loop structure that helps to solve this problem.

C++ offers the **do-while statement**:

.. code-block:: cpp
    :linenos:

    do
        statement; // can be a single statement or a compound statement
    while (condition);

A do while statement is a looping construct that works just like a while loop, except the statement always executes at least once. After the statement has been executed, the do-while loop checks the condition. If the condition evaluates to true, the path of execution jumps back to the top of the do-while loop and executes it again.

Here is an example using a do-while loop:

.. code-block:: cpp
    :linenos:

    int main()
    {
        // selection must be declared outside of the do-while so we can use it later
        int selection{};

        do
        {
            std::cout << "Please make a selection: \n";
            std::cout << "1) Addition\n";
            std::cout << "2) Subtraction\n";
            std::cout << "3) Multiplication\n";
            std::cout << "4) Division\n";
            std::cin >> selection;
        }
        while (selection != 1 && selection != 2 &&
            selection != 3 && selection != 4);

        // do something with selection here
        // such as a switch statement

        std::cout << "You selected option #" << selection << '\n';

        return 0;
    }

In practice, do-while loops aren't commonly used. Having the condition at the bottom of the loop obscures the loop condition, which can lead to errors. Many developers recommend avoiding do-while loops altogether as a result.
