######################################
C-Style Strings operations
######################################

C++ provides many functions to manipulate C-style strings as part of the ``<cstring>`` header.

``strcpy()`` allows you to copy a string to another string. More commonly, this is used to assign a value to a string:

.. code-block:: cpp
    :linenos:

    #include <cstring>
    #include <iostream>

    int main()
    {
        char source[]{ "Copy this!" };
        char dest[50];
        std::strcpy(dest, source);
        std::cout << dest << '\n'; // prints "Copy this!"

        return 0;
    }

However, ``strcpy()`` can easily cause array overflows if the destination array is shorter than the origin one.

Many programmers recommend using ``strncpy()`` instead, which allows you to specify the size of the buffer, and ensures overflow doesn't occur. Unfortunately, ``strncpy()`` doesn't ensure strings are null terminated, which still leaves plenty of room for array overflow.

``strlen()`` function returns the length of the C-style string (without the null terminator).

.. code-block:: cpp
    :linenos:

    #include <iostream>
    #include <cstring>
    #include <iterator> // for std::size

    int main()
    {
        char name[20]{ "Alex" }; // only use 5 characters (4 letters + null terminator)
        std::cout << "My name is: " << name << '\n';
        std::cout << name << " has " << std::strlen(name) << " letters.\n";
        std::cout << name << " has " << std::size(name) << " characters in the array.\n"; // use sizeof(name) / sizeof(name[0]) if not C++17 capable

        return 0;
    }

Note the difference between ``strlen()`` and ``std::size()``. ``strlen()`` prints the number of characters before the null terminator, whereas ``std::size`` (or the ``sizeof()`` trick) returns the size of the entire array, regardless of what's in it.

Other useful functions:
* ``strcat()``: Appends one string to another (dangerous)
* ``strncat()``: Appends one string to another (with buffer length check)
* ``strcmp()``: Compare two strings (returns 0 if equal)
* ``strncmp()``: Compare two strings up to a specific number of characters (returns 0 if equal)
