################################################
Variable assignment and initialization
################################################

Variable assignment
********************

After a variable has been defined, you can give it a value (in a separate statement) using the = operator. This process is called **copy assignment** (or just **assignment**) for short.

.. code-block:: cpp
    :linenos:

    int width; // define an integer variable named width
    width = 5; // copy assignment of value 5 into variable width

Copy assignment is named such because it copies the value on the right-hand side of the = operator to the variable on the left-hand side of the operator. The ``=`` operator is called the **assignment operator**.

When a new value is assigned to a variable, the value that was there previously is overwritten. Normal variables can only hold one value at a time.

.. warning::
    One of the most common mistakes is to confuse the assignment operator (=) with the equality operator (==). Assignment (=) is used to assign a value to a variable. Equality (==) is used to test whether two operands are equal in value.

Initialization
********************

One downside of assignment is that it requires at least two statements: one to define the variable, and one to assign the value.

These two steps can be combined. When a variable is defined, you can also provide an initial value for the variable at the same time. This is called **initialization**. The value used to initialize a variable is called an **initializer**.

There are 4 basic ways to initialize variables in C++:

.. code-block:: cpp
    :linenos:

    int a; // no initializer
    int b = 5; // initializer after equals sign
    int c( 6 ); // initializer in parenthesis
    int d { 7 }; // initializer in braces

Copy initialization
********************

When an initializer is provided after an equals sign, this is called **copy initialization**. Copy initialization was inherited from the C language.

.. code-block:: cpp

    int width = 5; // copy initialization of value 5 into variable width

Much like copy assignment, this copies the value on the right-hand side of the equals to the variable being created on the left-hand side.

For simple types like int, copy initialization is efficient. However, when types get more complex, copy initialization can be inefficient.

Direct initialization
***********************

When an initializer is provided inside parenthesis, this is called direct initialization.

.. code-block:: cpp

    int width(5); // direct initialization of value 5 into variable width

For simple data types (like int), copy and direct initialization are essentially the same. For more complicated types, direct initialization tends to be more efficient than copy initialization.

Brace initialization
**********************

Unfortunately, direct initialization can not be used for all types of initialization (such as initializing an object with a list of data). To provide a more consistent initialization mechanism, there is **brace initialization** (also called **uniform initialization** or **list initialization**) that uses curly braces.

Brace initialization comes in three forms:

.. code-block:: cpp
    :linenos:

    int width { 5 }; // direct brace initialization of value 5 into variable width (preferred)
    int height = { 6 }; // copy brace initialization of value 6 into variable height
    int depth {}; // default value initialization

Direct and copy brace initialization function almost identically, but the direct form is generally preferred.

Brace initialization has the added benefit of disallowing “narrowing” conversions. This means that if brace initialization is used to initialize a variable with a value it can not safely hold, the compiler will throw a warning or an error. For example:

.. code-block:: cpp

    int width { 4.5 }; // error: not all double values fit into an int

With brace initialization, the example above will cause the compiler to issue an error (which is generally a good thing).

Value initialization and zero initialization
*********************************************

When a variable is initialized with empty braces, **value initialization** takes place. In most cases, **value initialization** will initialize the variable to zero (or empty, if that is more appropriate for a given type). In such cases where zeroing occurs, this is called **zero initialization**.

.. code-block:: cpp

    int width {}; // zero initialization to value 0

Initializing multiple variables
********************************

Multiple variables can also be defined on the same line:

.. code-block:: cpp

    int a = 5, b = 6; // copy initialization
    int c( 7 ), d( 8 ); // direct initialization
    int e { 9 }, f { 10 }; // brace initialization (preferred)

Unfortunately, there is a common pitfall here that can occur when the programmer mistakenly tries to initialize both variables by using one initialization statement:

.. code-block:: cpp

    int a, b = 5; // wrong (a is not initialized!)
    int a = 5, b = 5; // correct
