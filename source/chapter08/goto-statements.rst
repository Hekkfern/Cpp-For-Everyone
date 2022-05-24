#############################
Goto statements
#############################

An unconditional jump causes execution to jump to another spot in the code. The term “unconditional” means the jump always happens (unlike an ``if statement`` or ``switch statement``, where the jump only happens conditionally based on the result of an expression).

In C++, unconditional jumps are implemented via a **goto statement**, and the spot to jump to is identified through use of a **statement label**.

The following is an example of a ``goto statement`` and ``statement label``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        double x{};
    tryAgain: // this is a statement label
        std::cout << "Enter a non-negative number: ";
        std::cin >> x;

        if (x < 0.0)
            goto tryAgain; // this is the goto statement

        std::cout << "The square root of " << x << " is " << std::sqrt(x) << '\n';
        return 0;
    }

Previously, two kinds of scope has been covered: local (block) scope, and file (global) scope. statement labels utilize a third kind of scope: **function scope**, which means the label is visible throughout the function even before its point of declaration. The ``goto statement`` and its corresponding ``statement label`` must appear in the same function.

A ``goto statement`` can jump backwards (to a preceding point in the function) or jump forward (to a later point in the function).

Statement labels must be associated with a statement (hence their name: they label a statement). If the end of the function need to be pointed, a ``null statement``(``;``without any other code) must be used.

There are two primary limitations to jumping:

* the code can jump only within the bounds of a single function (it isn't allowed to jump out of one function and into another),
* the code can't jump forward over the initialization of any variable that is still in scope at the location being jumped to.

For example:

.. code-block:: cpp
    :linenos:

    int main()
    {
        goto skip;   // error: this jump is illegal because...
        int x { 5 }; // this initialized variable is still in scope at statement label 'skip'
    skip:
        x += 3;      // what would this even evaluate to if x wasn't initialized?
        return 0;
    }

Note that the code can jump backwards over a variable initialization, and the variable will be re-initialized when the initialization is executed.
