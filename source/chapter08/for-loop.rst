#############################
For loop
#############################

By far, the most utilized loop statement in C++ is the for statement. The **for statement** (also called a **for loop**) is preferred when we have an obvious loop variable because it lets us easily and concisely define, initialize, test, and change the value of loop variables.

As of C++11, there are two different kinds of ``for loops``:

* classic ``for statement``
* ``range-based for statement``

Classic For statement
**********************

The ``for statement`` looks pretty simple in abstract:

.. code-block:: cpp
    :linenos:

    for (init-statement; condition; end-expression)
        statement

The easiest way to initially understand how a ``for statement`` works is to convert it into an equivalent ``while statement``:

.. code-block:: cpp
    :linenos:

    { // note the block here
        init-statement; // used to define variables used in the loop
        while (condition)
        {
            statement;
            end-expression; // used to modify the loop variable prior to reassessment of the condition
        }
    } // variables defined inside the loop go out of scope here

A for statement is evaluated in 3 parts:

First, the ``init-statement`` is executed. This only happens once when the loop is initiated. The ``init-statement`` is typically used for variable definition and initialization. These variables have “loop scope”, which really just is a form of block scope where these variables exist from the point of definition through the end of the loop statement. In the while-loop equivalent, it is noticed that the ``init-statement`` is inside a block that contains the loop, so the variables defined in the ``init-statement`` go out of scope when the block containing the loop ends.

Second, for each loop iteration, the condition is evaluated. If this evaluates to ``true``, the statement is executed. If this evaluates to ``false``, the loop terminates and execution continues with the next statement beyond the loop.

Finally, after the statement is executed, the end-expression is evaluated. Typically, this expression is used to increment or decrement the loop variables defined in the init-statement. After the end-expression has been evaluated, execution returns to the second step (and the condition is evaluated again).

An example of *for loop* is shown below:

.. code-block:: cpp
    :linenos:

    int main()
    {
        for (int count{ 1 }; count <= 10; ++count)
            std::cout << count << ' ';

        return 0;
    }

The above ``for loop`` is equivaled to the following ``while loop``:

.. code-block:: cpp
    :linenos:


    int main()
    {
        { // the block here ensures block scope for count
            int count{ 1 }; // our init-statement
            while (count <= 10) // our condition
            {
                std::cout << count << ' '; // our statement
                ++count; // our end-expression
            }
        }
    }

It is possible to write for loops that omit any or all of the statements or expressions. For example, omitting the init-statement and end-expression, leaving only the condition.

.. code-block:: cpp
    :linenos:

    int main()
    {
        int count{ 0 };
        for ( ; count < 10; ) // no init-statement or end-expression
        {
            std::cout << count << ' ';
            ++count;
        }

        return 0;
    }

Although ``for loops`` typically iterate over only one variable, sometimes ``for loops`` need to work with multiple variables. To assist with this, the programmer can define multiple variables in the ``init-statement``, and can make use of the comma operator to change the value of multiple variables in the ``end-expression``.

.. code-block:: cpp
    :linenos:

    int main()
    {
        for (int x{ 0 }, y{ 9 }; x < 10; ++x, --y)
            std::cout << x << ' ' << y << '\n';

        return 0;
    }

Range-based For Statement
**************************

There's a simpler and safer type of loop called a **for-each loop** (also called a **range-based for-loop**) for cases where it is wanted to iterate through every element in an array (or other list-type structure).

The for-each statement has a syntax that looks like this:

.. code-block:: cpp
    :linenos:

    for (element_declaration : array)
        statement;

When this statement is encountered, the loop will iterate through each element in array, assigning the value of the current array element to the variable declared in ``element_declaration``. For best results, ``element_declaration`` should have the same type as the array elements, otherwise type conversion will occur.

An example looks like this:

.. code-block:: cpp
    :linenos:

    int main()
    {
        constexpr int fibonacci[]{ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        for (int number : fibonacci) // iterate over array fibonacci
        {
            std::cout << number << ' '; // we access the array element for this iteration through variable number
        }

        std::cout << '\n';

        return 0;
    }

In the previous example, note that variable ``number`` is not an array index. It's assigned the value of the array element for the current loop iteration.

Because ``element_declaration`` should have the same type as the array elements, this is an ideal case in which to use the ``auto`` keyword, and let C++ deduce the type of the array elements.

Here's the above example, using auto:

.. code-block:: cpp
    :linenos:

    int main()
    {
        constexpr int fibonacci[]{ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        for (auto number : fibonacci) // type is auto, so number has its type deduced from the fibonacci array
        {
            std::cout << number << ' ';
        }

        std::cout << '\n';

        return 0;
    }

Each array element iterated over will be copied into variable ``element_declaration``. Copying array elements can be expensive, and most of the time we really just want to refer to the original element. Fortunately, references can be used for this.

.. code-block:: cpp
    :linenos:

    std::string array[]{ "peter", "likes", "frozen", "yogurt" };
    for (auto& element: array) // The ampersand makes element a reference to the actual array element, preventing a copy from being made
    {
        std::cout << element << ' ';
    }

``element`` will be a reference to the currently iterated array element, avoiding having to make a copy. Also any changes to element will affect the array being iterated over, something not possible if element is a normal variable.

And, of course, it's a good idea to make your reference const if it is intended to use it in a read-only fashion:

.. code-block:: cpp
    :linenos:

    std::string array[]{ "peter", "likes", "frozen", "yogurt" };
    for (const auto& element: array) // element is a const reference to the currently iterated array element
    {
        std::cout << element << ' ';
    }

``For-each loops`` don't only work with fixed arrays, they work with many kinds of list-like structures, such as vectors (e.g. ``std::vector``), linked lists, trees, and maps.

In order to iterate through the array, for-each needs to know how big the array is, which means knowing the array size. Because arrays that have decayed into a pointer do not know their size, for-each loops will not work with them!

Similarly, dynamic arrays won't work with for-each loops for the same reason.

For-each loops do not provide a direct way to get the array index of the current element. This is because many of the structures that for-each loops can be used with (such as linked lists) are not directly indexable!

However, since C++20, range-based for-loops can be used with an **init-statement** just like the ``init-statement`` in normal for-loops. The ``init-statement`` can be used to create a manual index counter without polluting the function in which the for-loop is placed.

The init-statement is placed right before the loop variable:

.. code-block:: cpp
    :linenos:

    for (init-statement; element_declaration : array)
        statement;
