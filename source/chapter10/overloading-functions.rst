#######################
Overloading functions
#######################

Consider the following function:

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    {
        return x + y;
    }

This trivial function adds two integers and returns an integer result. However, what if it is desired to have a function that can add two floating point numbers? This ``add()`` function is not suitable, as any floating point parameters would be converted to integers, causing the floating point arguments to lose their fractional values.

One way to work around this issue is to define multiple functions with slightly different names:

.. code-block:: cpp
    :linenos:

    int addInteger(int x, int y)
    {
        return x + y;
    }

    double addDouble(double x, double y)
    {
        return x + y;
    }

However, for best effect, this requires that you define a consistent function naming standard for similar functions that have parameters of different types, remember the names of these functions, and actually call the correct one.

And then what happens when it is wanted to have a similar function that uses 3 integers instead of 2? Managing unique names for each function quickly becomes burdensome.

Introduction to function overloading
*************************************

Fortunately, C++ has an elegant solution to handle such cases. Function overloading allows us to create multiple functions with the same name, so long as each identically named function has different parameter types (or the functions can be otherwise differentiated). Each function sharing a name (in the same scope) is called an overloaded function (sometimes called an overload for short).

To overload the ``add()`` function, it is simply required to declare another ``add()`` function that takes parameters of ``double`` type:

.. code-block:: cpp
    :linenos:

    double add(double x, double y)
    {
        return x + y;
    }

Now there are two versions of ``add()`` in the same scope:

.. code-block:: cpp
    :linenos:

    int add(int x, int y) // integer version
    {
        return x + y;
    }

    double add(double x, double y) // floating point version
    {
        return x + y;
    }

    int main()
    {
        return 0;
    }

The above program will compile. Although it might be expected these functions to result in a naming conflict, that is not the case here. Because the parameter types of these functions differ, the compiler is able to differentiate these functions, and will treat them as separate functions that just happen to share a name.

Functions can be overloaded so long as each overloaded function can be differentiated by the compiler. If an overloaded function can not be differentiated, a compile error will result.

Introduction to overload resolution
************************************

Additionally, when a function call is made to a function that has been overloaded, the compiler will try to match the function call to the appropriate overload based on the arguments used in the function call. This is called **overload resolution**.

Here's a simple example demonstrating this:

.. code-block:: cpp
    :linenos:

    int add(int x, int y)
    {
        return x + y;
    }

    double add(double x, double y)
    {
        return x + y;
    }

    int main()
    {
        std::cout << add(1, 2); // calls add(int, int)
        std::cout << '\n';
        std::cout << add(1.2, 3.4); // calls add(double, double)

        return 0;
    }

How overloaded functions are differentiated
*********************************************



Overloading based on number of parameters
*******************************************




Overloading based on type of parameters
****************************************



The return type of a function is not considered for differentiation
********************************************************************



Type signature
*****************

A function's **type signature** (generally called a **signature**) is defined as the parts of the function header that are used for differentiation of the function. In C++, this includes the function name, number of parameter, parameter type, and function-level qualifiers. It notably does *not* include the return type.

Name mangling
**************

When the compiler compiles a function, it performs **name mangling**, which means the compiled name of the function is altered ("mangled") based on various criteria, such as the number and type of parameters, so that the linker has unique names to work with.

For example, some function with prototype ``int fcn()`` might compile to name ``__fcn_v``, whereas ``int fcn(int)`` might compile to name ``__fcn_i``. So while in the source code, two overloaded functions share a name, in compiled code, the names are actually unique.

There is no standardization on how names should be mangled, so different compilers will produce different mangled names.
