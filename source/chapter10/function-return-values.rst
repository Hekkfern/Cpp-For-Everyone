#######################
Function return values
#######################

When a user-defined function is written, it is needed to determine whether the function will return a value back to the caller or not. To return a value back to the caller, two things are needed.

First, the function has to indicate what type of value will be returned. This is done by setting the function's **return type**, which is the type that is defined before the function's name. Note that this doesn't determine what specific value is returned; it only determines what type of value will be returned.

.. note::
Functions that return ``void`` are explored further in the lesson :ref:`void-functions`.

Second, inside the function that will return a value, we use a **return statement** to indicate the specific value being returned to the caller. The specific value returned from a function is called the **return value**. When the return statement is executed, the function exits immediately, and the return value is copied from the function back to the caller. This process is called **return by value**.

The following example shows a simple function that returns an integer value, and a sample program that calls it:

.. code-block:: cpp
    :linenos:

    // int is the return type
    // A return type of int means the function will return some integer value to the caller (the specific value is not specified here)
    int returnFive()
    {
        // the return statement indicates the specific value that will be returned
        return 5; // return the specific value 5 back to the caller
    }

    int main()
    {
        std::cout << returnFive() << '\n'; // prints 5
        std::cout << returnFive() + 2 << '\n'; // prints 7

        returnFive(); // okay: the value 5 is returned, but is ignored since main() doesn't do anything with it

        return 0;
    }

Return code of main()
***********************

When the program is executed, the operating system makes a function call to ``main``. Execution then jumps to the top of ``main``. The statements in ``main`` are executed sequentially. Finally, ``main`` returns an integer value (usually ``0``), and your program terminates. The return value from ``main`` is sometimes called a **status code** (also sometimes called an **exit code**, or rarely a **return code**), as it is used to indicate whether the program ran successfully or not.

By definition, a status code of ``0`` means the program executed successfully.

A non-zero status code is often used to indicate failure (and while this works fine on most operating systems, strictly speaking, it's not guaranteed to be portable).

The C++ standard only defines the meaning of 3 status codes: ``0``, ``EXIT_SUCCESS``, and ``EXIT_FAILURE``. ``0`` and ``EXIT_SUCCESS`` both mean the program executed successfully. ``EXIT_FAILURE`` means the program did not execute successfully.

``EXIT_SUCCESS`` and ``EXIT_FAILURE`` are defined in the ``<cstdlib>`` header:

.. code-block:: cpp
    :linenos:

    #include <cstdlib> // for EXIT_SUCCESS and EXIT_FAILURE

    int main()
    {
        return EXIT_SUCCESS;
    }

If maximizing portability is desired, only use ``0`` or ``EXIT_SUCCESS`` to indicate a successful termination, or ``EXIT_FAILURE`` to indicate an unsuccessful termination.

A value-returning function that does not return a value will produce undefined behavior
*****************************************************************************************

A function that returns a value is called a **value-returning function**. A function is value-returning if the return type is anything other than ``void``.

A value-returning function *must* return a value of that type (using a return statement), otherwise undefined behavior will result.

Here's an example of a function that produces undefined behavior:

.. code-block:: cpp
    :linenos:

    int getValueFromUser() // this function returns an integer value
    {
        std::cout << "Enter an integer: ";
        int input{};
        std::cin >> input;

        // note: no return statement
    }

    int main()
    {
        int num { getValueFromUser() }; // initialize num with the return value of getValueFromUser()

        std::cout << num << " doubled is: " << num * 2 << '\n';

        return 0;
    }

A modern compiler should generate a warning because the function is defined as returning a value but no return statement is provided.

In most cases, compilers will detect if returning a value have been forgotten. However, in some complicated cases, the compiler may not be able to properly determine whether your function returns a value or not in all cases, so developers should not rely on this.

Function main will implicitly return 0 if no return statement is provided
**************************************************************************

The only exception to the rule that a value-returning function must return a value via a return statement is for function ``main``. The function ``main`` will implicitly return the value ``0`` if no return statement is provided. That said, it is best practice to explicitly return a value from main, both to show your intent, and for consistency with other functions (which will not let developers omit the return value).

Functions can only return a single value
******************************************

A value-returning function can only return a single value back to the caller each time it is called.

Note that the value provided in a return statement doesn't need to be literal: it can be the result of any valid expression, including a variable or even a call to another function that returns a value.

There are various ways to work around the limitation of functions only being able to return a single value, which will be covered in future lessons.
