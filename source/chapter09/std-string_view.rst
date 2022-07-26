#################
std:string_view
#################

In order to avoid copying strings multiple times and so that, being expensive to initialize (or copy),  C++17 introduced ``std::string_view`` (which lives in the ``<string_view>`` header).

``std::string_view`` provides read-only access to an existing string (a C-style string literal, a ``std::string``, or a char array) without making a copy.

Unlike ``std::string``, which keeps its own copy of the string, ``std::string_view`` provides a view of a string that is defined elsewhere.

When a ``std::string_view`` is initialized with C-style string literal, the ``std::string_view`` provides read-only access to the string literal without making a copy of the string.

Unlike ``std::string``, ``std::string_view`` has full support for ``constexpr``:

.. code-block:: cpp
    :linenos:

    int main()
    {
        constexpr std::string_view s{ "Hello, world!" };
        std::cout << s << '\n'; // s will be replaced with "Hello, world!" at compile-time

        return 0;
    }

A ``std::string_view`` can be created using a ``std::string`` initializer, and a ``std::string`` will implicitly convert to a ``std::string_view``:

.. code-block:: cpp
    :linenos:

    void printSV(std::string_view str)
    {
        std::cout << str << '\n';
    }

    int main()
    {
        std::string s{ "Hello, world" };
        std::string_view sv{ s }; // Initialize a std::string_view from a std::string
        std::cout << sv;

        printSV(s); // implicitly convert a std::string to std::string_view

        return 0;
    }

Because ``std::string`` makes a copy of its initializer, C++ won't allow implicit conversion of a ``std::string`` from a ``std::string_view``. However, we can explicitly create a ``std::string`` with a ``std::string_view`` initializer, or we can convert an existing ``std::string_view`` to a ``std::string`` using ``static_cast``:

.. code-block:: cpp
    :linenos:

    void printString(std::string str)
    {
        std::cout << str << '\n';
    }

    int main()
    {
    std::string_view sv{ "balloon" };

    std::string str{ sv }; // okay, we can create std::string using std::string_view initializer

    // printString(sv);   // compile error: won't implicitly convert std::string_view to a std::string

    printString(static_cast<std::string>(sv)); // okay, we can explicitly cast a std::string_view to a std::string

    return 0;
    }

Double-quoted string literals are C-style string literals by default.Sstring literals can be created with type ``std::string_view`` by using a ``sv`` suffix after the double-quoted string literal.

.. code-block:: cpp
    :linenos:

    #include <iostream>
    #include <string>      // for std::string
    #include <string_view> // for std::string_view

    int main()
    {
        using namespace std::literals; // easiest way to access the s and sv suffixes

        std::cout << "foo\n";   // no suffix is a C-style string literal
        std::cout << "goo\n"s;  // s suffix is a std::string literal
        std::cout << "moo\n"sv; // sv suffix is a std::string_view literal

        return 0;
    };

Because ``std::string_view`` doesn't create a copy of the string, if the viewed string is changed, the changes are reflected in the ``std::string_view``.

.. code-block:: cpp
    :linenos:

    char arr[]{ "Gold" };
    std::string_view str{ arr };

    std::cout << str << '\n'; // Gold

    // Change 'd' to 'f' in arr
    arr[3] = 'f';

    std::cout << str << '\n'; // Gol

``std::string_view`` has many of the functions that also exist in ``std::string``:

.. code-block:: cpp
    :linenos:

    std::string_view str{ "Trains are fast!" };

    std::cout << str.length() << '\n'; // 16
    std::cout << str.substr(0, str.find(' ')) << '\n'; // Trains
    std::cout << (str == "Trains are fast!") << '\n'; // 1

    // Since C++20
    std::cout << str.starts_with("Boats") << '\n'; // 0
    std::cout << str.ends_with("fast!") << '\n'; // 1

    std::cout << str << '\n'; // Trains are fast!
