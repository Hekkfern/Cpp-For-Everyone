################
C++ Strings
################

The easiest way to work with strings and string objects in C++ is via the std::string type, which lives in the ``<string>`` header.

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

Strings can hold numbers as well. In string form, numbers are treated as text, not as numbers, and thus they can not be manipulated as numbers (e.g. they can't be multiplied). C++ will not automatically convert strings to integer or floating point values or vice-versa (although there are ways to do it manually).

To know how many characters are in a std::string, a std::string object can be asked for its length. The syntax for doing this is calling the ``length()``method inside the string object:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::string name{ "Alex" };
        std::cout << name << " has " << name.length() << " characters\n";

        return 0;
    }

The ``length()`` function isn't a normal standalone function: it's a special type of function that is nested within ``std::string`` called a member function. Because ``length()`` lives within ``std::string``, it is sometimes written as ``std::string::length()`` in documentation.

Also note that ``std::string::length()`` returns an unsigned integral value (most likely of type ``size_t``). Using static_cast is recommended to avoid compiler warnings about signed/unsigned conversions:

.. code-block:: cpp
    :linenos:

    int length { static_cast<int>(name.length()) };

In C++20, the ``std::ssize()`` function  can be used to get the length of a ``std::string`` as a signed integer:

.. code-block:: cpp
    :linenos:

    int main()
    {
        std::string name{ "Alex" };
        std::cout << name << " has " << std::ssize(name) << " characters\n";

        return 0;
    }

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
