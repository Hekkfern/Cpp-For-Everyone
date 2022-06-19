#####
Halts
#####

A **halt** is a flow control statement that terminates the program. In C++, halts are implemented as functions (rather than keywords), so halt statements will be function calls.

Let's take a brief detour, and recap what happens when a program exits normally. When the ``main()`` function returns (either by reaching the end of the function, or via a ``return statement``), a number of different things happen.

First, because we're leaving the function, all local variables and function parameters are destroyed (as per usual).

Next, a special function called ``std::exit()`` is called, with the return value from ``main()`` (the ``status code``) passed in as an argument.

``std::exit()`` is a function that causes the program to terminate normally. **Normal termination** means the program has exited in an expected way. Note that the term *normal termination* does not imply anything about whether the program was successful (that's what the ``status code`` is for).

``std::exit()`` performs a number of cleanup functions. First, objects with static storage duration are destroyed. Then some other miscellaneous file cleanup is done if any files were used. Finally, control is returned back to the OS, with the argument passed to ``std::exit()`` used as the status code.

Although ``std::exit()`` is called implicitly when function main() ends, ``std::exit()`` can also be called explicitly to halt the program before it would normally terminate. When ``std::exit()`` is called this way, it is needed to include the ``cstdlib`` header.

Here is an example of using ``std::exit()`` explicitly:

.. code-block:: cpp
    :linenos:

    #include <cstdlib> // for std::exit()
    #include <iostream>

    void cleanup()
    {
        // code here to do any kind of cleanup required
        std::cout << "cleanup!\n";
    }

    int main()
    {
        std::cout << 1 << '\n';
        cleanup();

        std::exit(0); // terminate and return status code 0 to operating system

        // The following statements never execute
        std::cout << 2 << '\n';

        return 0;
    }

Note that the statements after the call to ``std::exit()`` never execute because the program has already terminated.

One important note about calling ``std::exit()`` explicitly: ``std::exit()`` does not clean up any local variables (either in the current function, or in functions up the call stack). Because of this, it's generally better to avoid calling ``std::exit()``.

Because ``std::exit()`` terminates the program immediately, developers may want to manually do some cleanup before terminating. In this context, cleanup means things like closing database or network connections, deallocating any memory you have allocated, writing information to a log file, etc….

To assist with this, C++ offers the ``std::atexit()`` function, which allows you to specify a function that will automatically be called on program termination via ``std:exit()``.

Here's an example:

.. code-block:: cpp
    :linenos:


    #include <cstdlib> // for std::exit()
    #include <iostream>

    void cleanup()
    {
        // code here to do any kind of cleanup required
        std::cout << "cleanup!\n";
    }

    int main()
    {
        // register cleanup() to be called automatically when std::exit() is called
        std::atexit(cleanup); // note: we use cleanup rather than cleanup() since we're not making a function call to cleanup() right now

        std::cout << 1 << '\n';

        std::exit(0); // terminate and return status code 0 to operating system

        // The following statements never execute
        std::cout << 2 << '\n';

        return 0;
    }

So why would this tool be useful? It allows the developer to specify a cleanup function in one place (probably in ``main()``) and then not have to worry about remembering to call that function explicitly before calling ``std::exit()``.

A few notes here about ``std::atexit()`` and the cleanup function: first, because ``std::exit()`` is called implicitly when ``main()`` terminates, this will invoke any functions registered by ``std::atexit()`` if the program exits that way. Second, the function being registered must take no parameters and have no return value. Finally, multiple cleanup functions using ``std::atexit()`` can be registered if desired, and they will be called in reverse order of registration (the last one registered will be called first).

In multi-threaded programs, calling ``std::exit()`` can cause your program to crash (because the thread calling ``std::exit()`` will cleanup static objects that may still be accessed by other threads). For this reason, C++ has introduced another pair of functions that work similarly to ``std::exit()`` and ``std::atexit()`` called ``std::quick_exit()`` and ``std::at_quick_exit()``. ``std::quick_exit()`` terminates the program normally, but does not clean up static objects, and may or may not do other types of cleanup. ``std::at_quick_exit()`` performs the same role as ``std::atexit()`` for programs terminated with ``std::quick_exit()``.

The ``std::abort()`` function causes your program to terminate abnormally. **Abnormal termination** means the program had some kind of unusual runtime error and the program couldn't continue to run. For example, trying to divide by 0 will result in an abnormal termination. ``std::abort()`` does not do any cleanup.

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::cout << 1 << '\n';
        std::abort();

        // The following statements never execute
        std::cout << 2 << '\n';

        return 0;
    }

The ``std::terminate()`` function is typically used in conjunction with exceptions. Although ``std::terminate()`` can be called explicitly, it is more often called implicitly when an exception isn't handled (and in a few other exception-related cases). By default, ``std::terminate()`` calls ``std::abort()``.
