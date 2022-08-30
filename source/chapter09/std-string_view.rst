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

View modification functions
****************************

``std::string_view`` contains functions that let the users manipulate the view of the string. This allows them to change the view without modifying the viewed string. Similarly to a window with curtains: left or right curtain can be closed to reduce what the people can see.

The functions for this are ``remove_prefix``, which removes characters from the left side of the view, and ``remove_suffix``, which removes characters from the right side of the view.

.. code-block:: cpp
    :linenos:

    std::string_view str{ "Peach" };

    // Ignore the first character.
    str.remove_prefix(1);

    std::cout << str << '\n'; // prints "each"

    // Ignore the last 2 characters.
    str.remove_suffix(2);

    std::cout << str << '\n'; // prints "ea"

Unlike real curtains, a ``std::string_view`` cannot be opened back up. Once you shrink the area, the only way to re-widen it is to reset the view by reassigning the source string to it again.

``std::string_view`` works with non-null-terminated strings
*************************************************************

Unlike C-style strings and ``std::string``, ``std::string_view`` doesn't use null terminators to mark the end of the string. Rather, it knows where the string ends because it keeps track of its length.

.. code-block:: cpp
    :linenos:

    // No null-terminator.
    char vowels[]{ 'a', 'e', 'i', 'o', 'u' };

    // vowels isn't null-terminated. We need to pass the length manually.
    // Because vowels is an array, we can use std::size to get its length.
    std::string_view str{ vowels, std::size(vowels) };

    std::cout << str << '\n'; // This is safe. std::cout knows how to print std::string_view

Converting a ``std::string_view`` to a C-style string
*******************************************************

Some old functions (such as the old ``strlen`` function) still expect C-style strings. To convert a ``std::string_view`` to a C-style string, first it has to be converted to a ``std::string``:

.. code-block:: cpp
    :linenos:

    std::string_view sv{ "balloon" };

    sv.remove_suffix(3);

    // Create a std::string from the std::string_view
    std::string str{ sv };

    // Get the null-terminated C-style string.
    auto szNullTerminated{ str.c_str() };

    // Pass the null-terminated string to the function that we want to use.
    std::cout << str << " has " << std::strlen(szNullTerminated) << " letter(s)\n";

However, creating a ``std::string`` every time we want to pass a ``std::string_view`` as a C-style string is expensive, so this should be avoided if possible.

Passing strings by ``const std::string&`` or ``std::string_view``?
********************************************************************

If it is wanted to write a function that takes a string parameter, making the parameter a ``std::string_view`` is the most flexible choice, because it can work efficiently with C-style string arguments (including string literals), ``std::string`` arguments (which will implicitly convert to ``std::string_view``), and ``std::string_view`` arguments.

.. code-block:: cpp
    :linenos:

    void printSV(std::string_view sv)
    {
        std::cout << sv << '\n';
    }

    int main()
    {
        std::string s{ "Hello, world" };
        std::string_view sv { s };

        printSV(s);              // ok: pass std::string
        printSV(sv);             // ok: pass std::string_view
        printSV("Hello, world"); // ok: pass C-style string literal

        return 0;
    }

Note that ``std::string_view`` is passed by value instead of by const reference. This is because ``std::string_view`` is typically fast to copy, and pass by value is optimal for cheap to copy types.

There is one case where making the parameter a ``const std::string&`` is generally better: if the function needs to call some other function that takes a C-style string or ``std::string`` parameter, then ``const std::string&`` may be a better choice, as ``std::string_view`` is not guaranteed to be null-terminated (something that C-style string functions expect) and does not efficiently convert back to a ``std::string``.

Ownership issues
*******************

A ``std::string_view``'s lifetime is independent of that of the string it is viewing (meaning the string being viewed can be destroyed before the ``std::string_view`` object). If this happens, then accessing the ``std::string_view`` will cause undefined behavior.

The string that a ``std::string_view`` is viewing has to have been created somewhere else. It might be a string literal that lives as long as the program does, or a ``std::string``, in which case the string lives until the ``std::string`` decides to destroy it or the ``std::string dies``.

``std::string_view`` can't create any strings on its own, because it is just a view.

Opening the window (kinda) via the data() function
***************************************************

The string being viewed by a ``std::string_view`` can be accessed by using the ``data()`` function, which returns a C-style string. This provides fast access to the string being viewed (as a C-string). But it should also only be used if the ``std::string_view``'s view hasn't been modified (e.g. by ``remove_prefix`` or ``remove_suffix``) and the string being viewed is null-terminated.

When a ``std::string_view`` has been modified, ``data()`` doesn't always do what it is supposed to.
