###################################################
4.6 Boolean values
###################################################

Boolean variables
***********************************

**Boolean** variables are variables that can have only two possible values: ``true``, and ``false``.

To declare a Boolean variable, the keyword ``bool`` is used.

.. code-block:: cpp

    bool b;

To initialize or assign a true or false value to a Boolean variable, the keywords true and false are used.

.. code-block:: cpp
    :linenos:

    bool b1 { true };
    bool b2 { false };
    b1 = false;
    bool b3 {}; // default initialize to false

The logical **NOT operator** (``!``) can be used to flip a Boolean value from ``true`` to ``false``, or ``false`` to ``true``:

.. code-block:: cpp
    :linenos:

    bool b1 { !true }; // b1 will be initialized with the value false
    bool b2 { !false }; // b2 will be initialized with the value true

Boolean values are not actually stored in Boolean variables as the words “true” or “false”. Instead, they are stored as integers: ``true`` becomes the integer ``1``, and ``false`` becomes the integer ``0``. Similarly, when Boolean values are evaluated, they don't actually evaluate to “true” or “false”. They evaluate to the integers ``0`` (false) or ``1`` (true). Because Booleans actually store integers, they are considered an integral type.

Integer to Boolean conversion
*******************************

A Boolean can not be initialized with an integer using uniform initialization.

.. code-block:: cpp

    bool b{ 4 }; // error: narrowing conversions disallowed

However, in any context where an integer can be converted to a Boolean, the integer ``0`` is converted to ``false``, and any other integer is converted to ``true``.
