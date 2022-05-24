##################
Global variables
##################

In C++, variables can also be declared outside of a function. Such variables are called **global variables**.

By convention, global variables are declared at the top of a file, below the includes, but above any code.

Here's an example of a global variable being defined:

.. code-block:: cpp
    :linenos:

    #include <iostream>

    // Variables declared outside of a function are global variables
    int g_x {}; // global variable g_x

    void doSomething()
    {
        // global variables can be seen and used everywhere in the file
        g_x = 3;
        std::cout << g_x << '\n';
    }

    int main()
    {
        doSomething();
        std::cout << g_x << '\n';

        // global variables can be seen and used everywhere in the file
        g_x = 5;
        std::cout << g_x << '\n';

        return 0;
    }
    // g_x goes out of scope here

Global variables have **file scope** (also informally called **global scope** or **global namespace scope**), which means they are visible from the point of declaration until the end of the file in which they are declared. Once declared, a global variable can be used anywhere in the file from that point onward!

Because they are defined outside of a function, global variables are considered to be part of the global namespace (hence the term “global namespace scope”).

Global variables are created when the program starts, and destroyed when it ends. This is called **static duration**. Variables with *static duration* are sometimes called **static variables**.

Unlike local variables, which are uninitialized by default, static variables are zero-initialized by default.

Non-constant global variables can be optionally initialized:

.. code-block:: cpp
    :linenos:

    int g_x; // no explicit initializer (zero-initialized by default)
    int g_y {}; // zero initialized
    int g_z { 1 }; // initialized with value

Just like local variables, global variables can be constant. As with all constants, constant global variables must be initialized.

.. code-block:: cpp
    :linenos:

    #include <iostream>

    const int g_x; // error: constant variables must be initialized
    constexpr int g_w; // error: constexpr variables must be initialized

    const int g_y { 1 };  // const global variable g_y, initialized with a value
    constexpr int g_z { 2 }; // constexpr global variable g_z, initialized with a value

    void doSomething()
    {
        // global variables can be seen and used everywhere in the file
        std::cout << g_y << '\n';
        std::cout << g_z << '\n';
    }

    int main()
    {
        doSomething();

        // global variables can be seen and used everywhere in the file
        std::cout << g_y << '\n';
        std::cout << g_z << '\n';

        return 0;
    }
    // g_y and g_z goes out of scope here
