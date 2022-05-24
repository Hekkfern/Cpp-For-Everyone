#################################
Variable shadowing (name hiding)
#################################

What happens when there is a variable inside a nested block that has the same name as a variable in an outer block? When this happens, the nested variable “hides” the outer variable in areas where they are both in scope. This is called **name hiding** or **shadowing**.

Here's an example:

.. code-block:: cpp
    :linenos:

    int main()
    { // outer block
        int apples { 5 }; // here's the outer block apples

        { // nested block
            // apples refers to outer block apples here
            std::cout << apples << '\n'; // print value of outer block apples

            int apples{ 0 }; // define apples in the scope of the nested block

            // apples now refers to the nested block apples
            // the outer block apples is temporarily hidden

            apples = 10; // this assigns value 10 to nested block apples, not outer block apples

            std::cout << apples << '\n'; // print value of nested block apples
        } // nested block apples destroyed


        std::cout << apples << '\n'; // prints value of outer block apples

        return 0;
    } // outer block apples destroyed

Note that if any nested block variable with the same name has not been defined, the variable name in the nested block would still refer to the outer block variable, so any assignment or read of that variable would be applied to the outer block one.

.. code-block:: cpp
    :linenos:

    #include <iostream>

    int main()
    { // outer block
        int apples{5}; // here's the outer block apples

        { // nested block
            // apples refers to outer block apples here
            std::cout << apples << '\n'; // print value of outer block apples

            // no inner block apples defined in this example

            apples = 10; // this applies to outer block apples

            std::cout << apples << '\n'; // print value of outer block apples
        } // outer block apples retains its value even after we leave the nested block

        std::cout << apples << '\n'; // prints value of outer block apples

        return 0;
    } // outer block apples destroyed

Similar to how variables in a nested block can shadow variables in an outer block, local variables with the same name as a global variable will shadow the global variable wherever the local variable is in scope:

.. code-block:: cpp
    :linenos:

    #include <iostream>
    int value { 5 }; // global variable

    void foo()
    {
        std::cout << "global variable value: " << value << '\n'; // value is not shadowed here, so this refers to the global value
    }

    int main()
    {
        int value { 7 }; // hides the global variable value until the end of this block

        ++value; // increments local value, not global value

        std::cout << "local variable value: " << value << '\n';

        foo();

        return 0;
    } // local value is destroyed

However, because global variables are part of the global namespace, we can use the scope operator (::) with no prefix to tell the compiler we mean the global variable instead of the local variable.

.. code-block:: cpp
    :linenos:

    #include <iostream>
    int value { 5 }; // global variable

    int main()
    {
        int value { 7 }; // hides the global variable value
        ++value; // increments local value, not global value

        --(::value); // decrements global value, not local value (parenthesis added for readability)

        std::cout << "local variable value: " << value << '\n';
        std::cout << "global variable value: " << ::value << '\n';

        return 0;
    } // local value is destroyed

Shadowing of local variables should generally be avoided, as it can lead to inadvertent errors where the wrong variable is used or modified. Some compilers will issue a warning when a variable is shadowed.

For the same reason that it is recommended avoiding shadowing local variables, it is also recommended avoiding shadowing global variables as well. This is trivially avoidable if all of the global variable names use a `g_` prefix.
