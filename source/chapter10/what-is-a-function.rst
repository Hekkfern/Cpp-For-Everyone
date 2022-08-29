#######################
What is a Function?
#######################

Introduction
*************

A **function** is defined as a reusable sequence of statements designed to do a particular job..

every executable program must have a function named main (which is where the program starts execution when it is run). However, as programs start to get longer and longer, putting all the code inside the main function becomes increasingly hard to manage. Functions provide a way to split programs into small, modular chunks that are easier to organize, test, and use.

Functions that developers write on their own are called **user-defined functions**.

A **function call** is an expression that tells the CPU to interrupt the current function and execute another function. The CPU “puts a bookmark” at the current point of execution, and then **calls** (executes) the function named in the function call. When the called function ends, the CPU returns back to the point it bookmarked, and resumes execution.

The function initiating the function call is called the **caller**, and the function being called is the **callee** or **called** function.

An example of a user-defined function
**************************************

This is the most basic syntax to define a user-defined function:

.. code-block:: cpp
    :linenos:

    return-type identifier() // This is the function header (tells the compiler about the existence of the function)
    {
        // This is the function body (tells the compiler what the function does)
    }

The first line is called the **function header**, and it tells the compiler that a function is being defined, what the function is called, and some other information that will be covered in future lessons (like the return type and parameter types).

The curly braces and statements in-between are called the **function body**. This is where the statements that determine what your function does will go.

Calling functions more than once
*********************************

One useful thing about functions is that they can be called more than once. Here’s a program that demonstrates this:

.. code-block:: cpp
    :linenos:

    void doPrint()
    {
        std::cout << "In doPrint()\n";
    }

    // Definition of function main()
    int main()
    {
        std::cout << "Starting main()\n";
        doPrint(); // doPrint() called for the first time
        doPrint(); // doPrint() called for the second time
        std::cout << "Ending main()\n";

        return 0;
    }

Functions calling functions
****************************

Any function can call any other function.

In the following program, function ``main`` calls function ``doA``, which calls function ``doB``:

.. code-block:: cpp
    :linenos:

    void doB()
    {
        std::cout << "In doB()\n";
    }


    void doA()
    {
        std::cout << "Starting doA()\n";

        doB();

        std::cout << "Ending doA()\n";
    }

    // Definition of function main()
    int main()
    {
        std::cout << "Starting main()\n";

        doA();

        std::cout << "Ending main()\n";

        return 0;
    }

Nested functions are not supported
***********************************

Unlike some other programming languages, in C++, functions cannot be defined inside other functions.

The following program is not legal:

.. code-block:: cpp
    :linenos:

    int main()
    {
        void foo() // Illegal: this function is nested inside function main()
        {
            std::cout << "foo!\n";
        }

        foo(); // function call to foo()
        return 0;
    }

The proper way to write the above program is:

.. code-block:: cpp
    :linenos:

    void foo() // no longer inside of main()
    {
        std::cout << "foo!\n";
    }

    int main()
    {
        foo();
        return 0;
    }
