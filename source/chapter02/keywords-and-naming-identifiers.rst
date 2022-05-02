####################################
2.5 Keywords and naming identifiers
####################################

Keywords
********************

C++ reserves a set of 92 words (as of C++20) for its own use. These words are called **keywords** (or reserved words), and each of these keywords has a special meaning within the C++ language.

Here is a list of all the C++ keywords:

+-----------+---------------+-------------------+----------------+
| alignas   | const_cast    | int               | static_assert  |
+-----------+---------------+-------------------+----------------+
| alignof   | continue      | long              | static_cast    |
+-----------+---------------+-------------------+----------------+
| and       | co_await      | mutable           | struct         |
+-----------+---------------+-------------------+----------------+
| and_eq    | co_return     | namespace         | switch         |
+-----------+---------------+-------------------+----------------+
| asm       | co_yield      | new               | template       |
+-----------+---------------+-------------------+----------------+
| auto      | decltype      | noexcept          | this           |
+-----------+---------------+-------------------+----------------+
| bitand    | default       | not               | thread_local   |
+-----------+---------------+-------------------+----------------+
| bitor     | delete        | not_eq            | throw          |
+-----------+---------------+-------------------+----------------+
| bool      | do            | nullptr           | true           |
+-----------+---------------+-------------------+----------------+
| break     | double        | operator          | try            |
+-----------+---------------+-------------------+----------------+
| case      | dynamic_cast  | or                | typedef        |
+-----------+---------------+-------------------+----------------+
| catch     | else          | or_eq             | typeid         |
+-----------+---------------+-------------------+----------------+
| char      | enum          | private           | typename       |
+-----------+---------------+-------------------+----------------+
| char8_t   | explicit      | protected         | union          |
+-----------+---------------+-------------------+----------------+
| char16_t  | export        | public            | unsigned       |
+-----------+---------------+-------------------+----------------+
| char32_t  | extern        | register          | using          |
+-----------+---------------+-------------------+----------------+
| class     | false         | reinterpret_cast  | virtual        |
+-----------+---------------+-------------------+----------------+
| compl     | float         | requires          | void           |
+-----------+---------------+-------------------+----------------+
| concept   | for           | return            | volatile       |
+-----------+---------------+-------------------+----------------+
| const     | friend        | short             | wchar_t        |
+-----------+---------------+-------------------+----------------+
| consteval | goto          | signed            | while          |
+-----------+---------------+-------------------+----------------+
| constexpr | if            | sizeof            | xor            |
+-----------+---------------+-------------------+----------------+
| constinit | inline        | static            | xor_eq         |
+-----------+---------------+-------------------+----------------+

C++ also defines special identifiers: override, final, import, and module. These have a specific meaning when used in certain contexts but are not reserved.

Because keywords and special identifiers have special meaning, IDE (Integrated development environment) softwares will likely change the text color of these words to make them stand out from other identifiers.

Identifiers
********************

The name of a variable (or function, type, or other kind of item) is called an identifier. C++ gives a lot of flexibility to name identifiers.However, there are a few rules that must be followed when naming identifiers:

* The identifier can not be a keyword. Keywords are reserved.
* The identifier can only be composed of letters (lower or upper case), numbers, and the underscore character. That means the name can not contain symbols (except the underscore) nor whitespace (spaces or tabs).
* The identifier must begin with a letter (lower or upper case) or an underscore. It can not start with a number.
* C++ is case sensitive, and thus distinguishes between lower and upper case letters. For instance, "nvalue is different than "nValue" or "NVALUE".

Avoid naming your identifiers starting with an underscore, as these names are typically reserved for OS, library, and/or compiler use.

Identifiers should make clear what the value they are holding means (particularly if the units are not obvious). Identifiers should be named in a way that would help someone who has no idea what your code does be able to figure it out as quickly as possible.

An identifier with a trivial use can have a short name (e.g. such as i). An identifier that is used more broadly (e.g. a function that is called from many different places in a program) should have a longer and more descriptive name (e.g. instead of ``open``, try ``openFileOnDisk``).

In any case, avoid abbreviations. Although they reduce the time it is needed to write the code, they make the code harder to read. Even if the abbreviation is unambiguous, it takes the reader a moment to figure out what you meant. Code is read more often than it is written, the time it is saved while writing the code is time that every reader wastes when reading it.
