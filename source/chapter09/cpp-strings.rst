################
C++ Strings
################

The easiest way to work with strings and string objects in C++ is via the ``std::string type``, which lives in the ``<string>`` header.

``std::string`` is used for standard ascii and utf-8 strings. ``std::wstring`` is used for wide-character/unicode (utf-16) strings. There is no built-in class for utf-32 strings (though it could be extended from basic_string if it is needed).

Objects of type ``std::string`` can be created just like other objects:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::string name {}; // empty string

        return 0;
    }

Just like normal variables, they can be initialized or assigned values:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::string name { "Alex" }; // initialize name with string literal "Alex"
        name = "John";              // change name to "John"

        return 0;
    }

Strings can be created from a C-style string too:

.. code-block:: cpp
    :linenos:

    int main()
    {
        const char *szSource{ "my string" };
        std::string sOutput{ szSource };
        std::cout << sOutput << '\n';
    }

Strings can hold numbers as well. In string form, numbers are treated as text, not as numbers, and thus they can not be manipulated as numbers (e.g. they can't be multiplied). C++ will not automatically convert strings to integer or floating point values or vice-versa (although there are ways to do it manually). So, an statement like ``std::string sFour{ 4 };``will generate an error.

Whenever a ``std::string`` is initialized, a copy of the string used to initialize it is made. And whenever a ``std::string`` is passed by value to a ``std::string`` parameter, another copy is made. These copies are expensive, and should be avoided if possible.

Double-quoted string literals (like ``“Hello, world!”``) are C-style strings by default (and thus, have a strange type).

String literals can be created with type ``std::string`` by using a ``s`` suffix after the double-quoted string literal.

.. code-block:: cpp
    :linenos:

    int main()
    {
        using namespace std::literals; // easiest way to access the s and sv suffixes

        std::cout << "foo\n";   // no suffix is a C-style string literal
        std::cout << "goo\n"s;  // s suffix is a std::string literal

        return 0;
    };

If a ``constexpr std::string``is tried to be defined, your compiler will probably generate an error. This happens because ``constexpr std::string`` isn't supported in C++17 or earlier, and only has minimal support in C++20. If constexpr strings are needed, use std::string_view instead.
