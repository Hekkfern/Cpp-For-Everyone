#############################
Switch-case statement
#############################

Because testing a variable or expression for equality against a set of different values is common, C++ provides an alternative conditional statement called a **switch statement** that is specialized for this purpose.

.. code-block:: cpp
    :linenos:

    void printDigitName(int x)
    {
        switch (x)
        {
            case 1:
                std::cout << "One";
                return;
            case 2:
                std::cout << "Two";
                return;
            case 3:
                std::cout << "Three";
                return;
            default:
                std::cout << "Unknown";
                return;
        }
    }

    int main()
    {
        printDigitName(2);

        return 0;
    }

The idea behind a **switch statement** is simple: an expression (sometimes called the ``condition``) is evaluated to produce a value. If the expression’s value is equal to the value after any of the ``case labels``, the statements after the matching ``case label`` are executed. If no matching value can be found and a ``default label`` exists, the statements after the ``default label`` are executed instead.

Compared to the original ``if statement``, the ``switch statement`` has the advantage of only evaluating the expression once (making it more efficient), and the **switch statement** also makes it clearer to the reader that it is the same expression being tested for equality in each case.

A **switch statement** is started by using the ``switch`` keyword, followed by parentheses with the conditional expression that is going to be evaluated inside. Often the expression is just a single variable, but it can be any valid expression.

The one restriction is that the condition must evaluate to an integral type or an enumerated type, or be convertible to one. Expressions that evaluate to floating point types, strings, and most other non-integral types may not be used here.

Following the conditional expression, a block is declared. Inside the block, labels are used to define all of the values wanted to be tested for equality.

There are two kinds of labels: case labels and default labels.

The first kind of label is the **case label**, which is declared using the ``case`` keyword and followed by a constant expression. The constant expression must either match the type of the condition or must be convertible to that type.

If the value of the conditional expression equals the expression after a case label, execution begins at the first statement after that case label and then continues sequentially.

There is no practical limit to the number of case labels you can have, but all case labels in a switch must be unique.

The second kind of label is the **default label** (often called the **default case**), which is declared using the ``default`` keyword. If the conditional expression does not match any case label and a default label exists, execution begins at the first statement after the default label.

The default label is optional, and there can only be one default label per switch statement. By convention, the ``default case`` is placed last in the switch block.

A **break statement** (declared using the ``break`` keyword) tells the compiler that we are done executing statements within the switch, and that execution should continue with the statement after the end of the switch block. This allows us to exit a **switch statement** without exiting the entire function.

.. code-block:: cpp
    :linenos:

    switch (x) // x evaluates to 3
    {
        case 1:
            std::cout << "One";
            break;
        case 2:
            std::cout << "Two";
            break;
        case 3:
            std::cout << "Three"; // execution starts here
            break; // jump to the end of the switch block
        default:
            std::cout << "Unknown";
            break;
    }

When a switch expression matches a case label or optional default label, execution begins at the first statement following the matching label. Execution will then continue sequentially until one of the following termination conditions happens:

#. The end of the switch block is reached.
#. Another control flow statement (typically a break or return) causes the switch block or function to exit.
#. Something else interrupts the normal flow of the program (e.g. the OS shuts the program down, the universe implodes, etc…)

Note that the presence of another case label is not one of these terminating conditions; thus, without a ``break`` or ``return``, execution will overflow into subsequent cases.

Here is a program that exhibits this behavior:

.. code-block:: cpp
    :linenos:

    int main()
    {
        switch (2)
        {
        case 1: // Does not match
            std::cout << 1 << '\n'; // Skipped
        case 2: // Match!
            std::cout << 2 << '\n'; // Execution begins here
        case 3:
            std::cout << 3 << '\n'; // This is also executed
        case 4:
            std::cout << 4 << '\n'; // This is also executed
        default:
            std::cout << 5 << '\n'; // This is also executed
        }

        return 0;
    }

Once the statements underneath a case or default label have started executing, they will overflow (fallthrough) into subsequent cases. ``break`` or ``return`` statements are typically used to prevent this.

Since fallthrough is rarely desired or intentional, many compilers and code analysis tools will flag fallthrough as a warning.

Commenting intentional fallthrough is a common convention to tell other developers that fallthrough is intended. While this works for other developers, the compiler and code analysis tools don't know how to interpret comments, so it won't get rid of the warnings.

To help address this, C++17 adds a new attribute called ``[[fallthrough]]``.

**Attributes** are a modern C++ feature that allows the programmer to provide the compiler with some additional data about the code. To specify an attribute, the attribute name is placed between double hard braces. Attributes are not statements -- rather, they can be used almost anywhere where they are contextually relevant.

The ``[[fallthrough]]`` attribute modifies a null statement to indicate that fallthrough is intentional (and no warnings should be triggered).

.. code-block:: cpp
    :linenos:

    int main()
    {
        switch (2)
        {
        case 1:
            std::cout << 1 << '\n';
            break;
        case 2:
            std::cout << 2 << '\n'; // Execution begins here
            [[fallthrough]]; // intentional fallthrough --> note the semicolon to indicate the null statement
        case 3:
            std::cout << 3 << '\n'; // This is also executed
            break;
        }

        return 0;
    }

By placing multiple case labels in sequence, a statement can be used by multiple ``case statements``.

.. code-block:: cpp
    :linenos:

    bool isVowel(char c)
    {
        switch (c)
        {
            case 'a': // if c is 'a'
            case 'e': // or if c is 'e'
            case 'i': // or if c is 'i'
            case 'o': // or if c is 'o'
            case 'u': // or if c is 'u'
            case 'A': // or if c is 'A'
            case 'E': // or if c is 'E'
            case 'I': // or if c is 'I'
            case 'O': // or if c is 'O'
            case 'U': // or if c is 'U'
                return true;
            default:
                return false;
        }
    }

Remember, execution begins at the first statement after a matching case label. Case labels aren't statements (they're labels), so they don't count.

Thus, a “stack” of case labels can be used to make all of those case labels share the same set of statements afterward. This is not considered fallthrough behavior, so use of comments or ``[[fallthrough]]`` is not needed here.

With ``if statements``, you can only have a single statement after the if-condition, and that statement is considered to be implicitly inside a block. However, with switch statements, the statements after labels are all scoped to the the switch block. No implicit blocks are created.

Variables can be declared (but not initialized) inside the switch, both before and after the case labels.

.. code-block:: cpp
    :linenos:

    switch (1)
    {
        int a; // okay: declaration is allowed before the case labels
        int b{ 5 }; // illegal: initialization is not allowed before the case labels

        case 1:
            int y; // okay but bad practice: declaration is allowed within a case
            y = 4; // okay: assignment is allowed
            break;

        case 2:
            int z{ 4 }; // illegal: initialization is not allowed if subsequent cases exist
            y = 5; // okay: y was declared above, so we can use it here too
            break;

        case 3:
            break;
    }

Defining a variable without an initializer is just telling the compiler that the variable is now in scope from that point on. This happens at compile time, and doesn't require the definition to actually be executed at runtime.

However, initialization of variables does require execution at runtime. Initialization of variables is disallowed in any case that is not the last case (because the initializer could be jumped over, which would leave the variable uninitialized). Initialization is also disallowed before the first case, as those statements will never be executed, as there is no way for the switch to reach them.

If a case needs to define and/or initialize a new variable, best practice is to do so inside an explicit block underneath the case statement:

.. code-block:: cpp
    :linenos:

    switch (1)
    {
        case 1:
        { // note addition of explicit block here
            int x{ 4 }; // okay, variables can be initialized inside a block inside a case
            std::cout << x;
            break;
        }
        default:
            std::cout << "default case\n";
            break;
    }
