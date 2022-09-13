#######################
Function parameters
#######################

Function parameters and arguments
**********************************

In many cases, it is useful to be able to pass information to a function being called, so that the function has data to work with. For example, if it is wanted to write a function to add two numbers, it is required some way to tell the function which two numbers to add when it is called. Otherwise, how would the function know what to add? It is done via function parameters and arguments.

A **function parameter** is a variable used in a function. Function parameters work almost identically to variables defined inside the function, but with one difference: they are always initialized with a value provided by the caller of the function.

Function parameters are defined in the function declaration by placing them in between the parenthesis after the function identifier, with multiple parameters being separated by commas.

Here are some examples of functions with different numbers of parameters:

.. code-block:: cpp
    :linenos:

    // This function takes no parameters
    // It does not rely on the caller for anything
    void doPrint()
    {
        std::cout << "In doPrint()\n";
    }

    // This function takes one integer parameter named x
    // The caller will supply the value of x
    void printValue(int x)
    {
        std::cout << x  << '\n';
    }

    // This function has two integer parameters, one named x, and one named y
    // The caller will supply the value of both x and y
    int add(int x, int y)
    {
        return x + y;
    }

An **argument** is a value that is passed from the caller to the function when a function call is made:

.. code-block:: cpp
    :linenos:

    doPrint(); // this call has no arguments
    printValue(6); // 6 is the argument passed to function printValue()
    add(2, 3); // 2 and 3 are the arguments passed to function add()

Note that multiple arguments are also separated by commas.

How parameters and arguments work together
*******************************************

When a function is called, all of the parameters of the function are created as variables, and the value of each of the arguments is copied into the matching parameter. This process is called **pass by value**.

For example:

.. code-block:: cpp
    :linenos:

    // This function has two integer parameters, one named x, and one named y
    // The values of x and y are passed in by the caller
    void printValues(int x, int y)
    {
        std::cout << x << '\n';
        std::cout << y << '\n';
    }

    int main()
    {
        printValues(6, 7); // This function call has two arguments, 6 and 7

        return 0;
    }

Note that the number of arguments must generally match the number of function parameters, or the compiler will throw an error. The argument passed to a function can be any valid expression (as the argument is essentially just an initializer for the parameter, and initializers can be any valid expression).

Using return values as arguments
**********************************

The return value of one function can be used directly as an argument to another function.

For example:

.. code-block:: cpp
    :linenos:

    int getValueFromUser()
    {
        std::cout << "Enter an integer: ";
        int input{};
        std::cin >> input;

        return input;
    }

    void printDouble(int value)
    {
        std::cout << value << " doubled is: " << value * 2 << '\n';
    }

    int main()
    {
        // we’re using the return value of function getValueFromUser
        // directly as an argument to function printDouble
        printDouble(getValueFromUser());

        return 0;
    }
