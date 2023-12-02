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

The **address-of operator** (``&``) returns the memory address of its operand.

This is pretty straightforward:

.. code-block:: cpp
    :linenos:

    int main()
    {
        int x{ 5 };
        std::cout << x << '\n';  // print the value of variable x
        std::cout << &x << '\n'; // print the memory address of variable x

        return 0;
    }

In the above example, the address-of operator (``&``) is used to retrieve the address assigned to variable ``x`` and print that address to the console.

For objects that use more than one byte of memory, address-of will return the memory address of the first byte used by the object.

.. caution::

    The ``&`` symbol tends to cause confusion because it has different meanings depending on context:

    * When following a type name, ``&`` denotes an lvalue reference: ``int& ref``.
    * When used in a unary context in an expression, ``&`` is the address-of operator: ``std::cout << &x``.
    * When used in a binary context in an expression, ``&`` is the Bitwise AND operator: ``std::cout << x & y``.

The dereference operator (*)
*********************************

Getting the address of a variable isn't very useful by itself.

The most useful thing it can done with an address is accessing the value stored at that address. The **dereference operator** (``\*``) (also occasionally called the **indirection operator**) returns the value at a given memory address as an lvalue:

.. code-block:: cpp
    :linenos:

    int x{ 5 };
    std::cout << x << '\n';  // print the value of variable x
    std::cout << &x << '\n'; // print the memory address of variable x

    std::cout << *(&x) << '\n'; // print the value at the memory address of variable x (parentheses not required, but make it easier to read)

Given a memory address, the dereference operator (``\*``) can be used to get the value at that address (as an lvalue).

The address-of operator (``\&``) and dereference operator (``\*``) work as opposites: address-of gets the address of an object, and dereference gets the object at an address.

What is a Pointer?
*******************

A pointer is an object that holds a *memory address* (typically of another variable) as its value. This allows storing the address of some other object to use later.

.. note::

    In modern C++, the pointers showed in this page are sometimes called **raw pointers** or **dumb pointers**, to help differentiate them from **smart pointers** that were introduced into the language more recently. Smart pointers will be covered in :doc:`../chapter19/what-is-a-smart-pointer`.

Much like reference types are declared using an ampersand (``&``) character, pointer types are declared using an asterisk (``\*``):

.. code-block:: cpp
    :linenos:

    int;  // a normal int
    int&; // an lvalue reference to an int value
    int*; // a pointer to an int value (holds the address of an integer value)

To create a pointer variable, it is simply needed to define a variable with a pointer type:

.. code-block:: cpp
    :linenos:

    int x { 5 };    // normal variable
    int& ref { x }; // a reference to an integer (bound to x)

    int* ptr;       // a pointer to an integer

Note that this asterisk is part of the declaration syntax for pointers, not a use of the dereference operator.

.. danger::

    Although developers generally should not declare multiple variables on a single line, if it is done, the asterisk has to be included with each variable.

    .. code-block:: cpp
        :linenos:

        int* ptr1, ptr2;   // incorrect: ptr1 is a pointer to an int, but ptr2 is just a plain int!
        int* ptr3, * ptr4; // correct: ptr3 and p4 are both pointers to an int

    Although this is sometimes used as an argument to not place the asterisk with the type name (instead placing it next to the variable name), it's a better argument for avoiding defining multiple variables in the same statement.

Pointer initialization
***********************

Like normal variables, pointers are not initialized by default. A pointer that has not been initialized is sometimes called a **wild pointer**. Wild pointers contain a garbage address, and dereferencing a wild pointer will result in undefined behavior. Because of this, pointers should be always initialized to a known value.

.. code-block:: cpp
    :linenos:

    int x{ 5 };

    int* ptr;        // an uninitialized pointer (holds a garbage address)
    int* ptr2{};     // a null pointer (we'll discuss these in the next lesson)
    int* ptr3{ &x }; // a pointer initialized with the address of variable x

.. tip::

    Always initialize the pointers. At least, assign them ``nullptr`` temporarily until they obtain their final values.

Since pointers hold addresses, when they are initialized or assigned a value, that value has to be an address. Typically, pointers are used to hold the address of another variable (which it can be gotten by using the address-of operator (``&``)).

Once a pointer is holding the address of another object, the dereference operator (``\*``) can be used to access the value at that address. For example:

.. code-block:: cpp
    :linenos:

    int x{ 5 };
    std::cout << x << '\n'; // print the value of variable x

    int* ptr{ &x }; // ptr holds the address of x
    std::cout << *ptr << '\n'; // use dereference operator to print the value at the address that ptr is holding (which is x's address)

.. note::

    A note on pointer nomenclature: “X pointer” (where X is some type) is a commonly used shorthand for “pointer to an X”. So when it is said: “an integer pointer”, it is really meant “a pointer to an integer”.

Much like the type of a reference has to match the type of object being referred to, the type of the pointer has to match the type of the object being pointed to:

.. code-block:: cpp
    :linenos:

    int i{ 5 };
    double d{ 7.0 };

    int* iPtr{ &i };     // ok: a pointer to an int can point to an int object
    int* iPtr2 { &d };   // not okay: a pointer to an int can't point to a double
    double* dPtr{ &d };  // ok: a pointer to a double can point to a double object
    double* dPtr2{ &i }; // not okay: a pointer to a double can't point to an int

With one exception, initializing a pointer with a literal value is disallowed:

.. code-block:: cpp
    :linenos:

    int* ptr{ 5 }; // not okay
    int* ptr{ 0x0012FF7C }; // not okay, 0x0012FF7C is treated as an integer literal

Pointers and assignment
************************
