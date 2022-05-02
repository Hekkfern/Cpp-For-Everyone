################
Variables
################

Data
********************

**Data** is any information that can be moved, processed, or stored by a computer.

Data on a computer is typically stored in a format that is efficient for storage or processing (and is thus not human readable).

Objects and Variables
***********************

All computers have memory, called **RAM** (short for random access memory), that is available for the programs to use. RAM memory can be imagined as a series of numbered mailboxes that can each be used to hold a piece of data while the program is running. A single piece of data, stored in memory somewhere, is called a **value**.

In general programming, the term object typically refers to a variable, data structure in memory, or function. In C++, the term object has a narrower definition that excludes functions.

In C++, direct memory access is not allowed. Instead, memory is accessed indirectly through an object. An **object** is a region of storage (usually memory) that has a value and other associated properties.

Objects can be named or unnamed (anonymous). A named object is called a **variable**, and the name of the object is called an **identifier**.

Variable instantiation
***********************

In order to create a variable, a special kind of declaration statement called a **definition** is used.

An example of defining a variable named x:

.. code-block:: cpp

    int x; // define a variable named x, of type int

At compile time, when the compiler sees this statement, it makes a note to itself that a variable is being defined, giving it the name ``x``, and that it is of type ``int``. From that point forward, whenever the compiler sees the identifier x, it will know that this variable is being referenced.

When the program is run (called **runtime**), the variable will be instantiated. **Instantiation** means that the object will be created and assigned a memory address. Variables must be instantiated before they can be used to store values. An instantiated object is sometimes also called an **instance**.

It is possible to define multiple variables *of the same type* in a single statement by separating the names with a comma.

.. code-block:: cpp

    int a, b;
