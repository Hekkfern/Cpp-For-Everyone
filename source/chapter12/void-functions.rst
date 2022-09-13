#############################
Void functions
#############################

Void return values
*******************

Functions are not required to return a value back to the caller. To tell the compiler that a function does not return a value, a return type of ``void`` is used.

For example:

.. code-block:: cpp
    :linenos:

    // void means the function does not return a value to the caller
    void printHi()
    {
        std::cout << "Hi" << '\n';

        // This function does not return a value so no return statement is needed
    }

    int main()
    {
        printHi(); // okay: function printHi() is called, no value is returned

        return 0;
    }

A function that does not return a value is called a **non-value returning function** (or a **void function**).

Void functions don't need a return statement
*********************************************

A void function will automatically return to the caller at the end of the function. No return statement is required.

A return statement (with no return value) can be used in a void function. Such a statement will cause the function to return to the caller at the point where the return statement is executed. This is the same thing that happens at the end of the function anyway. Consequently, putting an empty return statement at the end of a void function is redundant.

.. code-block:: cpp
    :linenos:

    // void means the function does not return a value to the caller
    void printHi()
    {
        std::cout << "Hi" << '\n';

        return; // tell compiler to return to the caller -- this is redundant since this will happen anyway!
    } // function will return to caller here

    int main()
    {
        printHi();

        return 0;
    }

So, it is suggested not putting a return statement at the end of a non-value returning function.

Void functions can't be used in expression that require a value
****************************************************************

Some statements require values to be provided, and others don't.

When a function is called by itself, a function is called for its behavior, not its return value. In this case, it can be called either a non-value returning function; or a value-returning function and just ignore the return value.

When a function is called in a context that requires a value, a value must be provided. In such a context, value-returning functions are the only ones that can be called.

.. code-block:: cpp
    :linenos:

    // Function that does not return a value
    void returnNothing()
    {
    }

    // Function that returns a value
    int returnFive()
    {
        return 5;
    }

    int main()
    {
        // When calling a function by itself, no value is required
        returnNothing(); // ok: we can call a function that does not return a value
        returnFive();    // ok: we can call a function that returns a value, and ignore that return value

        // When calling a function in a context that requires a value (like std::cout)
        std::cout << returnFive();    // ok: we can call a function that returns a value, and the value will be used
        std::cout << returnNothing(); // compile error: we can't call a function that returns void in this context

        return 0;
    }

Returning a value from a void function is a compile error
**********************************************************

Trying to return a value from a non-value returning function will result in a compilation error:

.. code-block:: cpp
    :linenos:

    void printHi() // This function is non-value returning
    {
        std::cout << "In printHi()" << '\n';

        return 5; // compile error: we're trying to return a value
    }

Early returns
**************

A return statement that is not the last statement in a function is called a **early return**. Such a statement will cause the function to return to the caller when the return statement is executed (before the function would otherwise return to the caller, hence, “early”).

.. code-block:: cpp
    :linenos:

    void print() // note: void return type
    {
        std::cout << "A";

        return; // the function will return to the caller here (note: no return value)

        std::cout << "B"; // this will never be printed
    }

    int main()
    {
        print();

        return 0;
    }

Early returns can be used in value-returning functions too:

.. code-block:: cpp
    :linenos:

    int print() // note: return type of int
    {
        std::cout << "A";
        return 5; // the function will return to the caller here
        std::cout << "B"; // this will never be printed
    }

    int main()
    {
        std::cout << print(); // print() returns value 5, which will be print to the console

        return 0;
    }

Historically, early returns were frowned upon. However, in modern programming they are more accepted, particularly when they can be used to make a function simpler, or are used to abort a function early due to some error condition.
