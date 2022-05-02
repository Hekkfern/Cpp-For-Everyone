####################################
2.3 The main() function
####################################

The main function is a special function. Every C++ program must contain a function named main. It serves as the entry point for the program. The computer will start running the code from the beginning of the main function.

Types of `main()` function:

#. `main()` function without parameters

.. code-block:: cpp
    :linenos:

    int main() {
        ...
        return 0;
    }

#. `main()` function with parameters

.. code-block:: cpp
    :linenos:

    int main(int argc, char * const argv[]) {
        ...
        return 0;
    }

The reason for having the parameter option for the main function is to allow input from the command line.

When you use the main function with parameters, it saves every group of characters (separated by a space) after the program name as elements in an array named ``argv``.

Since the main function has the return type of int, the programmer must always have a return statement in the code. The number that is returned is used to inform the calling program what the result of the program's execution was. Returning 0 signals that there were no problems.
