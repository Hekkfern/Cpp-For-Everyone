####################
Internal linkage
####################

Introduction
************

An identifier with **internal linkage** can be seen and used within a single file, but it is not accessible from other files (that is, it is not exposed to the linker). This means that if two files have identically named identifiers with internal linkage, those identifiers will be treated as independent.

Internal objects (and functions) that are defined in different files are considered to be independent entities (even if their names and types are identical), so there is no violation of the one-definition rule. Each internal object only has one definition.

Global variables with internal linkage
***************************************

Global variables with internal linkage are sometimes called internal variables.

To make a non-constant global variable internal, use the ``static`` keyword.

.. code-block:: cpp
    :linenos:

    static int g_x; // non-constant globals have external linkage by default, but can be given internal linkage via the static keyword

    const int g_y { 1 }; // const globals have internal linkage by default
    constexpr int g_z { 2 }; // constexpr globals have internal linkage by default

    int main()
    {
        return 0;
    }

``const`` and ``constexpr`` global variables have internal linkage by default (and thus don't need the static keyword, so if it is used, it will be ignored).

Functions with internal linkage
********************************

Because linkage is a property of an identifier (not of a variable), function identifiers have the same linkage property that variable identifiers do. Functions default to external linkage, but can be set to internal linkage via the ``static`` keyword

.. code-block:: cpp
    :linenos:

    // This function is declared as static, and can now be used only within this file
    // Attempts to access it from another file via a function forward declaration will fail
    static int add(int x, int y)
    {
        return x + y;
    }
