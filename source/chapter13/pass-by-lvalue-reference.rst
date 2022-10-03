#########################
Pass by lvalue reference
#########################

Introduction
***************

In previous lessons, lvalue references were introduced (:doc:`../chapter11/lvalue-references`) and lvalue references to const (:doc:`../chapter11/lvalue-references-to-const`). In isolation, these may not have seemed very useful: why create an alias to a variable when the variable itself can just be used?

In this lesson, it will be finally provided some insight into what makes references useful.

First, some context. Back in lesson :doc:`function-parameters`, it was discussed ``pass by value``, where an argument passed to a function is copied into the function's parameter.

This means that when a function is called, a copy of the argument's value is made, only to use it briefly and then destroy it! Fortunately, because fundamental types are cheap to copy, this isn't a problem.

Some objects are expensive to copy
************************************

Most of the types provided by the standard library (such as ``std::string``) are ``class types``. Class types are usually expensive to copy. Whenever possible, it is wanted to avoid making unnecessary copies of objects that are expensive to copy, especially when those copies will be destroyed almost immediately.

Consider the following program illustrating this point:

.. code-block:: cpp
    :linenos:

    void printValue(std::string y)
    {
        std::cout << y << '\n';
    } // y is destroyed here

    int main()
    {
        std::string x { "Hello, world!" }; // x is a std::string

        printValue(x); // x is passed by value (copied) into parameter y (expensive)

        return 0;
    }

While this program behaves like it is expected, it's also inefficient. When ``printValue()`` is called, argument ``x`` is copied into ``printValue()`` parameter ``y``. However, in this example, the argument is a ``std::string`` instead of an ``int``, and ``std::string`` is a class type that is expensive to copy. And this expensive copy is made every time ``printValue()`` is called!

Pass by reference
******************

One way to avoid making an expensive copy of an argument when calling a function is to use ``pass by reference`` instead of ``pass by value``. When using **pass by reference**, a function parameter is declared as a reference type (or const reference type) rather than as a normal type. When the function is called, each reference parameter is bound to the appropriate argument. Because the reference acts as an alias for the argument, no copy of the argument is made.

Here's the same example as above, using ``pass by reference`` instead of ``pass by value``:

.. code-block:: cpp
    :linenos:

    void printValue(std::string& y) // type changed to std::string&
    {
        std::cout << y << '\n';
    } // y is destroyed here

    int main()
    {
        std::string x { "Hello, world!" };

        printValue(x); // x is now passed by reference into reference parameter y (inexpensive)

        return 0;
    }

This program is identical to the prior one, except the type of parameter ``y`` has been changed from ``std::string`` to ``std::string&`` (an lvalue reference). Now, when ``printValue(x)`` is called, lvalue reference parameter ``y`` is bound to argument ``x``. Binding a reference is always inexpensive, and no copy of ``x`` needs to be made. Because a reference acts as an alias for the object being referenced, when ``printValue()`` uses reference ``y``, it's accessing the actual argument ``x`` (rather than a copy of ``x``).

Pass by reference allows changing the value of an argument
****************************************************************

When an object is passed by value, the function parameter receives a copy of the argument. This means that any changes to the value of the parameter are made to the copy of the argument, not the argument itself:

.. code-block:: cpp
    :linenos:

    void addOne(int y) // y is a copy of x
    {
        ++y; // this modifies the copy of x, not the actual object x
    }

    int main()
    {
        int x { 5 };

        std::cout << "value = " << x << '\n';

        addOne(x);

        std::cout << "value = " << x << '\n'; // x has not been modified

        return 0;
    }

However, since a reference acts identically to the object being referenced, when using pass by reference, any changes made to the reference parameter will affect the argument:

.. code-block:: cpp
    :linenos:

    void addOne(int& y) // y is bound to the actual object x
    {
        ++y; // this modifies the actual object x
    }

    int main()
    {
        int x { 5 };

        std::cout << "value = " << x << '\n';

        addOne(x);

        std::cout << "value = " << x << '\n'; // x has been modified

        return 0;
    }

The ability for functions to modify the value of arguments passed in can be useful. Imagine a function that determines whether a monster has successfully attacked the player. If so, the monster should do some amount of damage to the player's health. If the player object is passed by reference, the function can directly modify the health of the actual player object that was passed in. If the player object is passed by value, the health of a copy of the player object could only be modify, which isn't as useful.

Pass by reference to non-const can only accept modifiable lvalue arguments
****************************************************************************

Because a reference to a non-const value can only bind to a modifiable lvalue (essentially a non-const variable), this means that pass by reference only works with arguments that are modifiable lvalues. In practical terms, this significantly limits the usefulness of pass by reference to non-const, as it means const variables or literals can not be passed.

For example:

.. code-block:: cpp
    :linenos:

    void printValue(int& y) // y only accepts modifiable lvalues
    {
        std::cout << y << '\n';
    }

    int main()
    {
        int x { 5 };
        printValue(x); // ok: x is a modifiable lvalue

        const int z { 5 };
        printValue(z); // error: z is a non-modifiable lvalue

        printValue(5); // error: 5 is an rvalue

        return 0;
    }

Fortunately, there's an easy way around this.

Pass by const reference
*************************

Unlike a reference to non-const (which can only bind to modifiable lvalues), a reference to const can bind to modifiable lvalues, non-modifiable lvalues, and rvalues. Therefore, if the reference parameter is made const, then it will be able to bind to any type of argument:

.. code-block:: cpp
    :linenos:

    void printValue(const int& y) // y is now a const reference
    {
        std::cout << y << '\n';
    }

    int main()
    {
        int x { 5 };
        printValue(x); // ok: x is a modifiable lvalue

        const int z { 5 };
        printValue(z); // ok: z is a non-modifiable lvalue

        printValue(5); // ok: 5 is a literal rvalue

        return 0;
    }

Passing by const reference offers the same primary benefit as pass by reference (avoiding making a copy of the argument), while also guaranteeing that the function can not change the value being referenced.

For example, the following is disallowed, because ref is const:

.. code-block:: cpp
    :linenos:

    void addOne(const int& ref)
    {
        ++ref; // not allowed: ref is const
    }


.. tip::

    Favor passing by const reference over passing by non-const reference unless you have a specific reason to do otherwise (e.g. the function needs to change the value of an argument).

Now the motivation for allowing const lvalue references to bind to rvalues is understood: without that capability, there would be no way to pass literals (or other rvalues) to functions that used pass by reference!

Mixing pass by value and pass by reference
********************************************

A function with multiple parameters can determine whether each parameter is passed by value or passed by reference individually.

For example:

.. code-block:: cpp
    :linenos:

    void foo(int a, int& b, const std::string& c)
    {
    }

    int main()
    {
        int x { 5 };
        const std::string s { "Hello, world!" };

        foo(5, x, s);

        return 0;
    }

In the above example, the first argument is passed by value, the second by reference, and the third by const reference.

When to pass by reference
***************************

Because class types can be expensive to copy (sometimes significantly so), class types are usually passed by const reference instead of by value to avoid making an expensive copy of the argument. Fundamental types are cheap to copy, so they are typically passed by value.

.. tip::

    Pass fundamental types by value, and class (or struct) types by const reference.

The cost of pass by value vs pass by reference
*************************************************

Not all class types need to be passed by reference. And you may be wondering why we don't just pass everything by reference. In this section, it is discussed the cost of pass by value vs pass by reference, and refine the best practice as to when each should be used.

There are two key points that will help to understand when pass by value or pass by reference should be used:

First, the cost of copying an object is generally proportional to two things:

* The size of the object. Objects that use more memory take more time to copy.
* Any additional setup costs. Some class types do additional setup when they are instantiated (e.g. such as opening a file or database, or allocating a certain amount of dynamic memory to hold an object of a variable size). These setup costs must be paid each time an object is copied.

On the other hand, binding a reference to an object is always fast (about the same speed as copying a fundamental type).

Second, accessing an object through a reference is slightly more expensive than accessing an object through a normal variable identifier. With a variable identifier, the compiler can just go to the memory address assigned to that variable and access the value. With a reference, there usually is an extra step: the compiler must first determine which object is being referenced, and only then can it go to that memory address for that object and access the value. The compiler can also sometimes optimize code using objects passed by value more highly than code using objects passed by reference. This means code generated for objects passed by reference is typically slower than the code generated for objects passed by value.

Now the question of why it is not passed everything by reference can be answered:

* For objects that are cheap to copy, the cost of copying is similar to the cost of binding, so pass by value is favored so the code generated will be faster.
* For objects that are expensive to copy, the cost of the copy dominates, so pass by (const) reference is favored to avoid making a copy.
