########################
Default arguments
########################

Introduction
******************

A default argument is a default value provided for a function parameter. For example:

.. code-block:: cpp
    :linenos:

    void print(int x, int y=10) // 10 is the default argument
    {
        std::cout << "x: " << x << '\n';
        std::cout << "y: " << y << '\n';
    }

When making a function call, the caller can optionally provide an argument for any function parameter that has a default argument. If the caller provides an argument, the value of the argument in the function call is used. If the caller does not provide an argument, the value of the default argument is used.

Note that the equals sign must be used to specify a default argument. Using parenthesis or brace initialization won't work:

.. code-block:: cpp
    :linenos:

    void foo(int x = 5);   // ok
    void goo(int x ( 5 )); // compile error
    void boo(int x { 5 }); // compile error

When to use default arguments
******************************

Default arguments are an excellent option when a function needs a value that has a reasonable default value, but for which it is wanted to let the caller override if they wish.

For example, here are a couple of function prototypes for which default arguments might be commonly used:

.. code-block:: cpp
    :linenos:

    int rollDie(int sides=6);
    void openLogFile(std::string filename="default.log");

Because the user can choose whether to supply a specific argument value or use the default value, a parameter with a default value provided is sometimes called an **optional parameter**. However, the term *optional* parameter is also used to refer to several other types of parameters (including parameters passed by address, and parameters using ``std::optional``), so it is recommended avoiding this term.

Multiple default arguments
***************************

A function can have multiple parameters with default arguments:

.. code-block:: cpp
    :linenos:

    void print(int x=10, int y=20, int z=30)
    {
        std::cout << "Values: " << x << " " << y << " " << z << '\n';
    }

    int main()
    {
        print(1, 2, 3); // all explicit arguments
        print(1, 2); // rightmost argument defaulted
        print(1); // two rightmost arguments defaulted
        print(); // all arguments defaulted

        return 0;
    }

C++ does not (as of C++20) support a function call syntax such as ``print(,,3)`` (as a way to provide an explicit value for ``z`` while using the default arguments for ``x`` and ``y``. This has two major consequences:

    1. Default arguments can only be supplied for the rightmost parameters. The following is not allowed:

    .. code-block:: cpp
        :linenos:

        void print(int x=10, int y); // not allowed

    2. If more than one default argument exists, the leftmost default argument should be the one most likely to be explicitly set by the user.

Default arguments can not be redeclared
*****************************************

Once declared, a default argument can not be redeclared (in the same file). That means for a function with a forward declaration and a function definition, the default argument can be declared in either the forward declaration or the function definition, but not both.

.. code-block:: cpp
    :linenos:

    void print(int x, int y=4); // forward declaration

    void print(int x, int y=4) // error: redefinition of default argument
    {
        std::cout << "x: " << x << '\n';
        std::cout << "y: " << y << '\n';
    }

Best practice is to declare the default argument in the forward declaration and not in the function definition, as the forward declaration is more likely to be seen by other files (particularly if it's in a header file).

Default arguments and function overloading
*******************************************

Functions with default arguments may be overloaded. For example, the following is allowed:

.. code-block:: cpp
    :linenos:

    void print(std::string string)
    {
    }

    void print(char ch=' ')
    {
    }

    int main()
    {
        print("Hello, world"); // resolves to print(std::string)
        print('a'); // resolves to print(char)
        print(); // resolves to print(char)

        return 0;
    }

Now consider this case:

.. code-block:: cpp
    :linenos:

    void print(int x);
    void print(int x, int y = 10);
    void print(int x, double y = 20.5);

Parameters with default values will differentiate a function overload (meaning the above will compile).
However, such functions can lead to potentially ambiguous function calls. For example:

.. code-block:: cpp
    :linenos:

    print(1, 2); // will resolve to print(int, int)
    print(1, 2.5); // will resolve to print(int, double)
    print(1); // ambiguous function call

In the last case, the compiler is unable to tell whether ``print(1)`` should resolve to ``print(int)`` or one of the two functions where the second parameter has a default value. The result is an ambiguous function call.
