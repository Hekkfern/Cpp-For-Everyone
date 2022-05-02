############
2.2 Comments
############

Introduction
===============

A comment is a programmer-readable note that is inserted directly into the source code of the program. Comments are ignored by the compiler and are for the programmer's use only.

In C++ there are two different styles of comments, both of which serve the same purpose: to help programmers document the code in some way.

Single-line comments
====================

The ``//`` symbol begins a C++ single-line comment, which tells the compiler to ignore everything from the ``//`` symbol to the end of the line.

.. code-block:: cpp

    std::cout << "Hello world!"; // Everything from here to the end of the line is ignored

Typically, the single-line comment is used to make a quick comment about a single line of code.

Having comments to the right of a line can make both the code and the comment hard to read, particularly if the line is long. However, if the lines are long, placing comments to the right can make your lines really long. In that case, single-line comments are often placed above the line it is commenting.

Multi-line comments
===================

The ``/*`` and ``*/`` pair of symbols denotes a C-style multi-line comment. Everything in between the symbols is ignored.

.. code-block:: cpp

    /* This is a multi-line comment.
       This line will be ignored.
       So will this one. */

Multi-line style comments can not be nested. When the compiler tries to compile it, it will ignore everything from the first ``/*`` to the first ``*/``. Since the rest of the comment is not surrounded by ``/*`` and ``*/``, the compiler will try to compile it. That will inevitably result in a compile error.

Don't use multi-line comments inside other multi-line comments. Wrapping single-line comments inside a multi-line comment is okay.

Commenting out code
===================

Converting one or more lines of code into a comment is called commenting out your code. This provides a convenient way to (temporarily) exclude parts of your code from being included in your compiled program.

To comment out a single line of code, simply use the ``//`` style comment to turn a line of code into a comment temporarily:

.. code-block:: cpp

    //    std::cout << 1;

To comment out a block of code, use ``//`` on multiple lines of code, or the ``/* */`` style comment to turn the block of code into a comment temporarily.
