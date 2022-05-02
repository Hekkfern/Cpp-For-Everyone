################
Preprocessor
################

Introduction
********************

The preprocessors are the directives, which give instructions to the compiler to preprocess the information before actual compilation starts.

All preprocessor directives begin with ``#``, and only white-space characters may appear before a preprocessor directive on a line. As soon as a newline character is found, the preprocessor directive is ends.

They are not C++ statements, so they do not end in a semicolon (``;``).

Each directive occupies one line. The only way a preprocessor directive can extend through more than one line is by preceding the newline character at the end of the line by a backslash (``\``).

There are number of preprocessor directives supported by C++ like ``#include``, ``#define``, ``#if``, ``#else``, ``#line``, etc.

The #define directive
***********************

The ``#define`` preprocessor directive creates symbolic constants. The symbolic constant is called a macro and the general form of the directive is:

.. code-block:: cpp

    #define macro-name replacement-text

When this line appears in a file, all subsequent occurrences of macro in that file will be replaced by replacement-text before the program is compiled.

Defined macros are not affected by block structure. A macro lasts until it is undefined with the ``#undef`` preprocessor directive.

You can use ``#define`` to define a macro which will take argument as follows:

.. code-block:: cpp

    #define MIN(a,b) (((a)<(b)) ? a : b)

It generates a sort of function (Function-Like Macros) which is substituted before the program is compiled.

Conditional compilation
************************

There are several directives, which can be used to compile selective portions of the program's source code. This process is called "conditional compilation".

The conditional preprocessor construct is much like the ``if`` selection structure.

It is controlled by directives ``#if``, ``#ifdef``, ``#ifndef``, ``#else``, ``#elif``, and ``#endif``.

The ``#if`` clause allows preprocessor to access its content if the associated statement is "true", or is a number different than ``0``.

.. code-block:: cpp
    :linenos:

    #if STATEMENT_1
        code
    #elif STATEMENT_2
        code
    #else
        code
    #endif

``#ifdef`` clause means "if defined", so preprocessor is going to execute its content if a ``#define`` clause has previously created that variable.

On the other hand, ``#ifndef`` clause means "if not defined", so preprocessor is going to execute its content if that variable has not already been created.

The #include directive
***********************

When the preprocessor finds an #include directive it replaces it by the entire content of the specified header or file.

There are two ways to use ``#include``:

.. code-block:: cpp
    :linenos:

    #include <header>
    #include "file"

In the first case, a header is specified between angle-brackets ``<>``. This is used to include headers provided by the implementation, such as the headers that compose the standard library. Whether the headers are actually files or exist in some other form is implementation-defined, but in any case they shall be properly included with this directive.

The syntax used in the second ``#include`` uses quotes, and includes a file. The file is searched for in an implementation-defined manner, which generally includes the current path. In the case that the file is not found, the compiler interprets the directive as a header inclusion, just as if the quotes (``""``) were replaced by angle-brackets (``<>``).

The #error directive
*********************

This directive aborts the compilation process when it is found, generating a compilation error that can be specified as its parameter:

.. code-block:: cpp
    :linenos:

    #ifndef STATEMENT
        #error A defined variable is required!
    #endif

Predefined macros
********************

There are some macros that are generated automatically during the translation, and can be used:

For example, ``__cplusplus`` denotes the version of C++ standard that is being used, or ``__DATE__`` and ``__TIME__`` expands to the date/time of the preprocessor translation.

More information about all these macros can be found in `Predefined macros <https://en.cppreference.com/w/cpp/preprocessor/replace#Predefined_macros>`_.

Also, the standard defines a set of preprocessor macros corresponding to C++ language features. They are intended as a simple and portable way to detect the presence of said features. See `Feature testing <https://en.cppreference.com/w/cpp/feature_test>`_ for details.
