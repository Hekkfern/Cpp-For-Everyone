#############################
Compound statements (blocks)
#############################

A **compound statement** (also called a **block**, or **block statement**) is a group of *zero or more statements* that is treated by the compiler as if it were a single statement.

Blocks begin with a ``{`` symbol, end with a ``}`` symbol, with the statements to be executed being placed in between. Blocks can be used anywhere a single statement is allowed. No semicolon is needed at the end of a block.

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    { // block
        return x + y;
    } // end block

Blocks can be nested inside other blocks. When blocks are nested, the enclosing block is typically called the **outer block** and the enclosed block is called the **inner block** or **nested block**.

.. code-block:: cpp
    :linenos:

    int main()
    { // outer block

        // multiple statements
        int value {};

        { // inner/nested block
            add(3, 4);
        } // end inner/nested block

        return 0;

    } // end outer block

    