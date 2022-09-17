# Style Guide

- [Style Guide](#style-guide)
  - [File structure and Filenames](#file-structure-and-filenames)
  - [Whitespaces](#whitespaces)
    - [Indentation](#indentation)
    - [Blank lines](#blank-lines)
    - [Line length](#line-length)
  - [Headings](#headings)
  - [Code blocks](#code-blocks)

## File structure and Filenames

Use only lowercase alphanumeric characters and ``-`` (minus) symbol.

Suffix filenames with the .rst extension.

## Whitespaces

### Indentation

Indent with 2 spaces.

### Blank lines

Two blank lines before overlined sections, i.e. before H1 and H2. One blank line before other sections.

One blank line to separate directives.

```text
Some text before.

.. note::

  Some note.
```

### Line length

No limits in the length of the lines.

## Headings

Use the following symbols to create headings:

1. # with overline
2. * with overline
3. =
4. -
5. ^
6. "

As an example:

```text
##################
H1: document title
##################

Introduction text.


*********
Sample H2
*********

Sample content.


**********
Another H2
**********

Sample H3
=========

Sample H4
---------

Sample H5
^^^^^^^^^

Sample H6
"""""""""

And some text.
```

If you need more than heading level 4 (i.e. H5 or H6), then you should consider creating a new document.

There should be only one H1 in a document.

## Code blocks

Use the ``code-block`` directive and specify the programming language. As an example:

```text
.. code-block:: cpp

  #include <stdlib.h>
```
