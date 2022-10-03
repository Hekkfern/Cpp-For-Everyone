#####################################
Pointers
#####################################

Introduction
************

Consider a normal variable, like this one:

.. code-block:: cpp
    :linenos:

    char x {}; // chars use 1 byte of memory

Simplifying a bit, when the code generated for this definition is executed, a piece of memory from RAM will be assigned to this object. For the sake of example, let's say that the variable ``x`` is assigned memory address ``140``. Whenever variable ``x`` is used in an expression or statement, the program will go to memory address ``140`` to access the value stored there.

The nice thing about variables is that developers don't need to worry about what specific memory addresses are assigned, or how many bytes are required to store the object's value. Variables are just referred by its given identifier, and the compiler translates this name into the appropriately assigned memory address. The compiler takes care of all the addressing.

This is also true with references:

.. code-block:: cpp
    :linenos:

    int main()
    {
        char x {}; // assume this is assigned memory address 140
        char& ref { x }; // ref is an lvalue reference to x (when used with a type, & means lvalue reference)

        return 0;
    }

Because ``ref`` acts as an alias for ``x``, whenever ``ref`` is used, the program will go to memory address ``140`` to access the value. Again the compiler takes care of the addressing, so that developers don't have to think about it.

The address-of operator (&)
****************************
