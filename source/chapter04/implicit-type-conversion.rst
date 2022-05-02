###############################
Implicit type conversion
###############################

What is the implicit type conversion?
***************************************

Implicit type conversion (also called automatic type conversion or coercion) is performed automatically by the compiler when one data type is required, but a different data type is supplied. The vast majority of type conversions in C++ are implicit type conversions.

For example, implicit type conversion happens in all of the following cases:

* When initializing (or assigning a value to) a variable with a value of a different data type:

.. code-block:: cpp

    double d{ 3 }; // int value 3 implicitly converted to type double
    d = 6; // int value 6 implicitly converted to type double

* When the type of a return value is different from the function's declared return type:

.. code-block:: cpp

    float doSomething()
    {
        return 3.0; // double value 3.0 implicitly converted to type float
    }

* When using certain binary operators with operands of different types:

.. code-block:: cpp

    double division{ 4.0 / 3 }; // int value 3 implicitly converted to type double

* When using a non-Boolean value in an if-statement:

.. code-block:: cpp

    if (5) // int value 5 implicitly converted to type bool
    {
    }

* When an argument passed to a function is a different type than the function parameter:

.. code-block:: cpp

    void doSomething(long l)
    {
    }

    doSomething(3); // int value 3 implicitly converted to type long

What happens when a type conversion is invoked
*************************************************

When a type conversion is invoked (whether implicitly or explicitly), the compiler will determine whether it can convert the value from the current type to the desired type. If a valid conversion can be found, then the compiler will produce a new value of the desired type. Note that type conversions don't change the value or type of the value or object being converted.

If the compiler can't find an acceptable conversion, then the compilation will fail with a compile error. Type conversions can fail for any number of reasons. For example, the compiler might not know how to convert a value between the original type and the desired type.

In other cases, statements may disallow certain types of conversions. Such conversions are disallowed when using brace-initialization.

.. code-block:: cpp

    int x { 3.5 }; // brace-initialization disallows conversions that result in data loss

There are also cases where the compiler may not be able to figure out which of several possible type conversions is unambiguously the best one to use.
