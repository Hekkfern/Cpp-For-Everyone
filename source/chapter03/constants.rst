###################################################
3.5 Constants
###################################################

Using #define macros for constants
***********************************

``#define`` statements can be used as a sort of constants definition solution. Whenever the preprocessor encounters this directive, any further occurrence of the identifier is replaced by its substitution text. The identifier is traditionally typed in all capital letters, using underscores to represent spaces.

So why is not recommended using ``#define`` to make symbolic constants? There are some major problems:

* While debugging the code, the actual value of the macro is not seen (only see the name of the symbolic constants). And because these defined values aren't variables, they can't be watched in the debugger to see their values. This can make programs harder to debug.
* Macros can have naming conflicts with normal code. If some header happened to #define a macro and overwrite its value, the preprocessor would replace the identifier with this last value, generating undesired results.
* Macros don't follow normal scoping rules, which means in rare cases a macro defined in one part of a program can conflict with code written in another part of the program that it wasn't supposed to interact with.
* Macros don't have any kind of *type* checking. Compiler won't notice if a macro value matches the expected type where it is used.

Const variables
****************

It's sometimes useful to define variables with values that can not be changed, so it can't be modified accidentally.

To make a variable constant, simply put the ``const`` keyword either before or after the variable type, like so:

.. code-block:: cpp

    const double gravity { 9.8 };

Constant variables are sometimes called **symbolic constants** (as opposed to literal constants, which are just values that have no name).

Const variables must be initialized when you define them, and then that value can not be changed via assignment.

Note that const variables can be initialized from other variables (including non-const ones). For example:

.. code-block:: cpp
    :linenos:

    std::cout << "Enter your age: ";
    int age{};
    std::cin >> age;

    const int usersAge { age };

Runtime vs compile-time constants
**********************************

C++ actually has two different kinds of constants.

**Runtime constants** are constants whose initialization values can only be resolved at runtime (when the program is running). However, once initialized, the value of these constants can't be changed.

The following example shows a runtime constant:

.. code-block:: cpp
    :linenos:

    std::cout << "Enter your age: ";
    int age{};
    std::cin >> age;

    const int usersAge { age }; // usersAge is a runtime constant because the value isn't known until the program is run

**Compile-time constants** are constants whose initialization values can be determined at compile-time (when the program is compiling).

Compile-time constants enable the compiler to perform optimizations that aren't available with runtime constants.

The following example shows a compile-time constant:

.. code-block:: cpp
    :linenos:

    const double gravity { 9.8 }; // the compiler knows at compile-time that gravity will have value 9.8
    const int something { 1 + 2 }; // the compiler can resolve this at compiler time

constexpr
************

C++ has the keyword ``constexpr``, which ensures that a constant must be a compile-time constant.

.. code-block:: cpp
    :linenos:

    constexpr double gravity { 9.8 }; // ok, the value of 9.8 can be resolved at compile-time
    constexpr int sum { 4 + 5 }; // ok, the value of 4 + 5 can be resolved at compile-time

    std::cout << "Enter your age: ";
    int age{};
    std::cin >> age;

    constexpr int myAge { age }; // compile error: age is a runtime constant, not a compile-time constant

Note that literals are also implicitly constexpr, as the value of a literal is known at compile-time.

Constant expressions
**********************

A **constant expression** is an expression that can be evaluated at compile-time.

.. code-block:: cpp
    :linenos:

    constexpr int x { 3 };
    constexpr int y { 4 };
    std::cout << x + y; // x + y evaluated at compile-time

The advantages, compared to using literals, is that the base values of the expression have custom names which helps developers to understand the meaning of those specific values.

Constant casting
******************

``const_cast`` is one of the type casting operators. It is used to change the constant value of any object or we can say it is used to remove the constant nature of any object.

``const_cast`` can be used in programs that have any object with some constant value which need to be changed occasionally at some point.

The syntax is as follows:

.. code-block:: cpp

    const_cast<type name>(expression)

It is commonly used to pass constant data to another function that does not accept constant data.

.. code-block:: cpp
    :linenos:

    int change(int* p2) {
        return (*p2 * 10);
    }
    int main() {
        const int num = 100;
        const int *p = &num;
        int *p1 = const_cast <int *>(p);
        cout << change(p1);
        return 0;
    }
