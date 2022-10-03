#####################################################
Type deduction with pointers, references, and const
#####################################################

In previous lesson :doc:`../chapter04/type-deduction-for-objects-using-the-auto-keyword`, it was discussed how the ``auto`` keyword can be used to have the compiler deduce the type of a variable from the initializer.

It was also noted that by default, type deduction will drop const qualifiers. So const must be reapplied by adding the ``const`` qualifier in the definition.

Type deduction drops references
********************************

In addition to dropping const qualifiers, type deduction will also drop references:

.. code-block:: cpp
    :linenos:

    std::string& getRef(); // some function that returns a reference

    int main()
    {
        auto ref { getRef() }; // type deduced as std::string (not std::string&)

        return 0;
    }

In the above example, variable ``ref`` is using type deduction. Although function ``getRef()`` returns a ``std::string&``, the reference qualifier is dropped, so the type of ``ref`` is deduced as ``std::string``.

Just like with the dropped ``const`` qualifier, if you want the deduced type to be a reference, you can reapply the reference at the point of definition:

.. code-block:: cpp
    :linenos:

    std::string& getRef(); // some function that returns a reference to const

    int main()
    {
        auto ref1 { getRef() };  // std::string (reference dropped)
        auto& ref2 { getRef() }; // std::string& (reference reapplied)

        return 0;
    }

Top-level const and low-level const
************************************

A **top-level** const is a const qualifier that applies to an object itself. For example:

.. code-block:: cpp
    :linenos:

    const int x;    // this const applies to x, so it is top-level
    int* const ptr; // this const applies to ptr, so it is top-level

In contrast, a **low-level const** is a const qualifier that applies to the object being referenced or pointed to:

.. code-block:: cpp
    :linenos:

    const int& ref; // this const applies to the object being referenced, so it is low-level
    const int* ptr; // this const applies to the object being pointed to, so it is low-level

A reference to a const value is always a low-level const. A pointer can have a top-level, low-level, or both kinds of const:

.. code-block:: cpp
    :linenos:

    const int* const ptr; // the left const is low-level, the right const is top-level

When it is said that type deduction drops const qualifiers, it only drops top-level consts. Low-level consts are not dropped.

Type deduction and const references
************************************

If the initializer is a reference to const, the reference is dropped first (and then reapplied if applicable), and then any top-level const is dropped from the result.

.. code-block:: cpp
    :linenos:

    const std::string& getRef(); // some function that returns a reference to const

    int main()
    {
        auto ref1{ getRef() }; // std::string (reference dropped, then top-level const dropped from result)

        return 0;
    }

In the above example, since ``getRef()`` returns a ``const std::string&``, the reference is dropped first, leaving us with a ``const std::string``. This const is now a top-level const, so it is also dropped, leaving the deduced type as ``std::string``.

We can reapply either or both of these:

.. code-block:: cpp
    :linenos:

    const std::string& getRef(); // some function that returns a const reference

    int main()
    {
        auto ref1{ getRef() };        // std::string (top-level const and reference dropped)
        const auto ref2{ getRef() };  // const std::string (const reapplied, reference dropped)

        auto& ref3{ getRef() };       // const std::string& (reference reapplied, low-level const not dropped)
        const auto& ref4{ getRef() }; // const std::string& (reference and const reapplied)

        return 0;
    }

We covered the case for ``ref1`` in the prior example. For ``ref2``, this is similar to the ``ref1`` case, except the ``const`` qualifier has been reapplied, so the deduced type is ``const std::string``.

Things get more interesting with ``ref3``. Normally the reference would be dropped, but since the reference has been reapplied, it is not dropped. That means the type is still ``const std::string&``. And since this const is a low-level const, it is not dropped. Thus the deduced type is ``const std::string&``.

The ``ref4`` case works similarly to ``ref3``, except the ``const`` qualifier has been reapplied as well. Since the type is already deduced as a reference to const, reapplying const here is redundant. That said, using ``const`` here makes it explicitly clear that the result will be const (whereas in the ``ref3`` case, the constness of the result is implicit and not obvious).

Type deduction and pointers
****************************

Unlike references, type deduction does not drop pointers:

.. code-block:: cpp
    :linenos:

    std::string* getPtr(); // some function that returns a pointer

    int main()
    {
        auto ptr1{ getPtr() }; // std::string*

        return 0;
    }

When ``auto`` is used with a pointer type initializer, the type deduced for ``auto`` includes the pointer. So for ``ptr1`` above, the type substituted for ``auto`` is ``std::string*``.

An asterisk can also be used in conjunction with pointer type deduction:

.. code-block:: cpp
    :linenos:

    std::string* getPtr(); // some function that returns a pointer

    int main()
    {
        auto ptr1{ getPtr() };  // std::string*
        auto* ptr2{ getPtr() }; // std::string*

        return 0;
    }

When ``auto*`` is used with a pointer type initializer, the type deduced for ``auto`` does not include the pointer (the pointer is reapplied afterward after the type is deduced). So for ``ptr2`` above, the type substituted for ``auto`` is ``std::string``, and then the pointer is reapplied.


The difference between auto and auto*
***************************************

In most cases, the practical effect is the same (see examples shown in :ref:`chapter10/type-deduction-with-pointers-references-and-const:Type deduction and pointers`).

However, there are a couple of difference between ``auto`` and ``auto*`` in practice. First, ``auto*`` must resolve to a pointer initializer, otherwise a compile error will result:

.. code-block:: cpp
    :linenos:

    std::string* getPtr(); // some function that returns a pointer

    int main()
    {
        auto ptr3{ *getPtr() };      // std::string (because we dereferenced getPtr())
        auto* ptr4{ *getPtr() };     // does not compile (initializer not a pointer)

        return 0;
    }

This makes sense: in the ``ptr4`` case, ``auto`` deduces to ``std::string``, then the pointer is reapplied. Thus ``ptr4`` has type ``std::string*``, and we can't initialize a ``std::string*`` with an initializer that is not a pointer.

Second, there are differences in how ``auto`` and ``auto*`` behave when we introduce const into the equation. This will be covered in :ref:`chapter10/type-deduction-with-pointers-references-and-const:Type deduction and const pointers`.

Type deduction and const pointers
*************************************

Since pointers aren't dropped, developers don't have to worry about that. But with pointers, both the const pointer and the pointer to const have cases to think about, and there is also ``auto`` vs ``auto*``. Just like with references, only top-level const is dropped during pointer type deduction.

A simple case:

.. code-block:: cpp
    :linenos:

    std::string* getPtr(); // some function that returns a pointer

    int main()
    {
        const auto ptr1{ getPtr() };  // std::string* const
        auto const ptr2 { getPtr() }; // std::string* const

        const auto* ptr3{ getPtr() }; // const std::string*
        auto* const ptr4{ getPtr() }; // std::string* const

        return 0;
    }

When either ``auto const`` or ``const auto`` are used, it is meant to say something as “make whatever the deduced type is const”. So in the case of ``ptr1`` and ``ptr2``, the deduced type is ``std::string*``, and then const is applied, making the final type ``std::string* const``. This is similar to how ``const int`` and ``int const`` mean the same thing.

However, when ``auto*`` is used, the order of the const qualifier matters. A ``const`` on the left means “make the deduced pointer type a pointer to const”, whereas a ``const`` on the right means “make the deduced pointer type a const pointer”. Thus ``ptr3`` ends up as a pointer to const, and ``ptr4`` ends up as a const pointer.

Now there is an example where the initializer is a const pointer to const.`

.. code-block:: cpp
    :linenos:

    const std::string* const getConstPtr(); // some function that returns a const pointer to a const value

    int main()
    {
        auto ptr1{ getConstPtr() };  // const std::string*
        auto* ptr2{ getConstPtr() }; // const std::string*

        auto const ptr3{ getConstPtr() };  // const std::string* const
        const auto ptr4{ getConstPtr() };  // const std::string* const

        auto* const ptr5{ getConstPtr() }; // const std::string* const
        const auto* ptr6{ getConstPtr() }; // const std::string*

        const auto const ptr7{ getConstPtr() };  // error: const qualifer can not be applied twice
        const auto* const ptr8{ getConstPtr() }; // const std::string* const

        return 0;
    }

The ``ptr1`` and ``ptr2`` cases are straightforward. The top-level const (the const on the pointer itself) is dropped. The low-level const on the object being pointed to is not dropped. So in both cases, the final type is ``const std::string*``.

The ``ptr3`` and ``ptr4`` cases are also straightforward. The top-level const is dropped, but it is reapplied. The low-level const on the object being pointed to is not dropped. So in both cases, the final type is ``const std::string* const``.

The ``ptr5`` and ``ptr6`` cases are analogous to the cases shown in the prior example. In both cases, the top-level const is dropped. For ``ptr5``, the ``auto* const`` reapplies the top-level const, so the final type is ``const std::string* const``. For ``ptr6``, the ``const auto*`` applies const to the type being pointed to (which in this case was already const), so the final type is ``const std::string*``.

In the ``ptr7`` case, the const qualifier is applied twice, which is disallowed, and will cause a compile error.

And finally, in the ``ptr8`` case, const is applied on both sides of the pointer (which is allowed since ``auto*`` must be a pointer type), so the resulting types is ``const std::string* const``.

So, to sum up, it a const pointer is wanted, the const qualifier has to be reapplied even when it's not strictly necessary, as it makes the intent clear and helps prevent mistakes.
