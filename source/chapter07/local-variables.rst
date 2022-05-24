#################
Local variables
#################

Function parameters, as well as variables defined inside the function body, are called **local variables**.

Function parameters are created and initialized when the function is entered, and variables within the function body are created and initialized at the point of definition.

Local variables are destroyed in the opposite order of creation at the end of the set of curly braces in which it is defined (or for a function parameter, at the end of the function).

.. code-block:: cpp
    :linenos:

    int main()
    {
        int i { 5 }; // i enters scope here
        double d { 4.0 }; // d enters scope here

        return 0;
    } // i and d go out of scope here

Local variables have **automatic storage duration**, which means they are created at the point of definition and destroyed at the end of the block they are defined in. For this reason, local variables are sometimes called **automatic variables**.

Local variables can be defined inside nested blocks. This works identically to local variables in function body blocks.

.. code-block:: cpp
    :linenos:

    int main() // outer block
    {
        int x { 5 }; // x enters scope and is created here

        { // nested block
            int y { 7 }; // y enters scope and is created here
        } // y goes out of scope and is destroyed here

        // y can not be used here because it is out of scope in this block

        return 0;
    } // x goes out of scope and is destroyed here

Note that nested blocks are considered part of the scope of the outer block in which they are defined. Consequently, variables defined in the outer block can be seen inside a nested block.

.. code-block:: cpp
    :linenos:

    int main()
    { // outer block

        int x { 5 }; // x enters scope and is created here

        { // nested block
            int y { 7 }; // y enters scope and is created here

            // x and y are both in scope here
            std::cout << x << " + " << y << " = " << x + y << '\n';
        } // y goes out of scope and is destroyed here

        // y can not be used here because it is out of scope in this block

        return 0;
    } // x goes out of scope and is destroyed here

Local variables have no linkage, which means that each declaration refers to a unique object.

.. code-block:: cpp
    :linenos:

    int main()
    {
        int x { 2 }; // local variable, no linkage

        {
            int x { 3 }; // this identifier x refers to a different object than the previous x
        }

        return 0;
    }

If a variable is only used within a nested block, it should be defined inside that nested block.

By limiting the scope of a variable, the complexity of the program is reduced because the number of active variables is lower. Further, it makes it easier to see where variables are used (or aren't used). A variable defined inside a block can only be used within that block (or nested blocks). This can make the program easier to understand.

On the other hand, if a variable is needed in an outer block, it needs to be declared in the outer block.
