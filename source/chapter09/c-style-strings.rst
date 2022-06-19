################
C-Style Strings
################

A **C-style string** is simply an array of characters that uses a null terminator. A **null terminator** is a special character (``\0``, ascii code 0) used to indicate the end of the string. More generically, a C-style string is called a **null-terminated string**.

To define a C-style string, simply declare a char array and initialize it with a string literal:

.. code-block:: cpp
    :linenos:

    char myString[]{ "string" };

C++ automatically adds a null terminator to the end of the literal strings. So, the size of the array of chars is actually one character larger than the number of letters.

When declaring strings in this manner, it is a good idea to use ``[]`` and let the compiler calculate the length of the array. That way if the string is changed later, adjusting the array length manually wouldn't be necessary.

Note that it's fine if the array is larger than the string it contains:

.. code-block:: cpp
    :linenos:

    int main()
    {
        char name[20]{ "Alex" }; // only use 5 characters (4 letters + null terminator)
        std::cout << "My name is: " << name << '\n';

        return 0;
    }

One important point to note is that C-style strings follow all the same rules as arrays. This means the string can be initialized upon creation, but values can not be assigned to it using the assignment operator after that!

.. code-block:: cpp
    :linenos:

    char myString[]{ "string" }; // ok
    myString = "rope"; // not ok!

Since C-style strings are arrays, the ``[]`` operator can be used to change individual characters in the string:

.. code-block:: cpp
    :linenos:

    int main()
    {
        char myString[]{ "string" };
        myString[1] = 'p';
        std::cout << myString << '\n';

        return 0;
    }

It is important to know about C-style strings because they are used in a lot of code. However, unless there is a compelling reason to use C-style strings, use ``std::string`` (defined in the ``<string>`` header) instead. ``std::string`` is easier, safer, and more flexible. In the rare case that it is nedded to work with fixed buffer sizes and C-style strings (e.g. for memory-limited devices), it is recommended using ``std::string_view``.
