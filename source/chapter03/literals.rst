###################################################
3.4 Literals
###################################################

Literal constants
************************

Literal constants (usually just called literals) are unnamed values inserted directly into the code.

.. code-block:: cpp
    :linenos:

    return 5; // 5 is an integer literal
    bool myNameIsAlex { true }; // true is a boolean literal
    std::cout << 3.4; // 3.4 is a double literal

They are constants because their values can not be changed dynamically (developers have to change them manually, and then recompile for the change to take effect).

Just like objects have a type, all literals have a type. The type of a literal is assumed from the value and format of the literal itself.

By default:

+-----------------------+------------------+-----------------+
| Literal value         | Examples         | Default type    |
+=======================+==================+=================+
| integral value        | 5, 0, -3         | int             |
+-----------------------+------------------+-----------------+
| boolean value         | true, false      | bool            |
+-----------------------+------------------+-----------------+
| floating point value  | 3.4, -2.2        | double          |
+-----------------------+------------------+-----------------+
| char value            | 'a'              | char            |
+-----------------------+------------------+-----------------+
| C-style string        | "Hello, world!"  | const char[14]  |
+-----------------------+------------------+-----------------+

If the default type of a literal is not as desired, the type of a literal can be changed by adding a suffix:

+------------+--------------------------------------------+----------------------+
| Data Type  | Suffix                                     | Meaning              |
+============+============================================+======================+
| int        | u or U                                     | unsigned int         |
+------------+--------------------------------------------+----------------------+
| int        | l or L                                     | long                 |
+------------+--------------------------------------------+----------------------+
| int        | ul, uL, Ul, UL, lu, lU, Lu, or LU          | unsigned long        |
+------------+--------------------------------------------+----------------------+
| int        | ll or LL                                   | long long            |
+------------+--------------------------------------------+----------------------+
| int        | ull, uLL, Ull, ULL, llu, llU, LLu, or LLU  | unsigned long long   |
+------------+--------------------------------------------+----------------------+
| double     | f or F                                     | float                |
+------------+--------------------------------------------+----------------------+
| double     | l or L                                     | long double          |
+------------+--------------------------------------------+----------------------+

Literals are fine to use in C++ code so long as their meanings are clear. This is most often the case when used to initialize or assign a value to a variable, do math, or print some text to the screen.

String literals
****************

C++ supports string literals as a group of characters surrounded with ``""``. For example, ``"Hello World!"``.

Scientific notation for floating point literals
************************************************

There are two different ways to declare floating-point literals. In order to use "scientific notation", the ``e`` character must be used to separate the module from the exponent.

.. code-block:: cpp
    :linenos:

    double pi { 3.14159 }; // 3.14159 is a double literal in standard notation
    double avogadro { 6.02e23 }; // 6.02 x 10^23 is a double literal in scientific notation

Octal and hexadecimal literals
*******************************

By default, numbers in C++ programs are assumed to be **decimal**. Decimal is also called “base 10”, because there are 10 possible digits (0 through 9).

.. code-block:: cpp
    :linenos:

    int x { 12 }; // 12 is assumed to be a decimal number
    int x{ 012 }; // 0 before the number means this is octal
    int x{ 0xF }; // 0x before the number means this is hexadecimal
    int x{ 0b1 }; // 0b before the number means this is binary

Because long literals can be hard to read, C++ also adds the ability to use a quotation mark (``'``) as a digit separator. Also note that the separator can not occur before the first digit of the value. For example:

.. code-block:: cpp
    :linenos:

    int bin { 0b1011'0010 };  // assign binary 1011 0010 to the variable
    long value { 2'132'673'462 }; // much easier to read than 2132673462
