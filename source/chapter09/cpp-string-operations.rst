######################
C++ String operations
######################

To know how many characters are in a ``std::string``, a ``std::string`` object can be asked for its length. The syntax for doing this is calling the ``length()`` method inside the string object:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::string name{ "Alex" };
        std::cout << name << " has " << name.length() << " characters\n";

        return 0;
    }

The ``length()`` function isn't a normal standalone function: it's a special type of function that is nested within ``std::string`` called a member function. Because ``length()`` lives within ``std::string``, it is sometimes written as ``std::string::length()`` in documentation.

This method returns the current number of characters in the string, excluding the null terminator.

Also note that ``std::string::length()`` returns an unsigned integral value (most likely of type ``size_t``). Using static_cast is recommended to avoid compiler warnings about signed/unsigned conversions:

.. code-block:: cpp
    :linenos:

    int length { static_cast<int>(name.length()) };

The method ``size()``of the ``std::string``class generates the same result. Both functions are equal.

In C++20, the ``std::ssize()`` function  can be used to get the length of a ``std::string`` as a signed integer:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::string name{ "Alex" };
        std::cout << name << " has " << std::ssize(name) << " characters\n";

        return 0;
    }

Although it's possible to use ``length()`` to determine whether a string has any characters or not, it's more efficient to use the ``empty()`` function. It returns ``true`` if the string has no characters, ``false`` otherwise.

.. code-block:: cpp
    :linenos:

    string string1 { "Not Empty" };
    std::cout << (string1.empty() ? "true" : "false") << '\n';


The capacity of a string reflects how much memory the string allocated to hold its contents. This value is measured in string characters, excluding the NULL terminator. For example, a string with capacity 8 could hold 8 characters.

So, the ``capacity()``method returns the number of characters a string can hold without reallocation.

.. code-block:: cpp
    :linenos:

    string s { "01234567" };
    std::cout << "Length: " << s.length() << '\n';
    std::cout << "Capacity: " << s.capacity() << '\n';

There are two almost identical ways to access characters in a string. The easier to use and faster version is the overloaded ``operator[]``.

.. code-block:: cpp
    :linenos:

    std::string sSource{ "abcdefg" };
    std::cout << sSource[5] << '\n';
    sSource[5] = 'X';
    std::cout << sSource << '\n';

There is also a non-operator version. This version is slower since it uses exceptions to check if the provided index is valid. If it is unsure whether nIndex is valid, this version should be used to access the array.

.. code-block:: cpp
    :linenos:

    std::string sSource{ "abcdefg" };
    std::cout << sSource.at(5) << '\n';
    sSource.at(5) = 'X';
    std::cout << sSource << '\n';

Many functions (including all C functions) expect strings to be formatted as C-style strings rather than ``std::string``. For this reason, ``std::string`` provides three different ways to convert ``std::string`` to C-style strings.

``c_str()`` returns the contents of the string as a const C-style string. A null terminator is appended. The C-style string is owned by the std::string and should not be deleted.

.. code-block:: cpp
    :linenos:

    std::string sSource{ "abcdefg" };
    std::cout << std::strlen(sSource.c_str());

``data()`` performs the same action as ``c_str()``. So, it returns the contents of the string as a const C-style string. A null terminator is appended. And the C-style string is owned by the std::string and should not be deleted.

``copy()`` copy at most nLength characters of the string to szBuf, beginning with character nIndex, returning the number of characters copied. No null is appended. It is up to the caller to ensure szBuf is initialized to NULL or terminate the string using the returned length. And the caller is responsible for not overflowing szBuf.







Unless every bit of efficiency is needed, ``c_str()`` is the easiest and safest of the three functions to use.
