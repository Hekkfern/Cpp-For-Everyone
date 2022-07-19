#####################
Forward declarations
#####################

Forward Declaration of functions in C++
****************************************

A **forward declaration** is the declaration of a function's syntax, i.e., its name, return type, arguments, and the data type of arguments before it is used in the program.

Before defining functions, forward declarations are included to let the compiler know the function is defined somewhere in the program. Forward declaration of functions used in a separate file is formed using the #include to have the file.

.. code-block:: cpp
    :linenos:

    #include <iostream>
    using namespace std;

    //forward declaration of sub2
    int sub2(int A, int B);

    int main()
    {
        cout << "Difference: " << sub2(25, 10);
        return 0;
    }

    int sub2(int A, int B) //Defining sub2 here
    {
        return A - B;
    }

Which is equivalent, without forward declaration, to:

.. code-block:: cpp
    :linenos:

    #include <iostream>
    using namespace std;

    int sub2(int A, int B) //Defining sub2 here
    {
        return A - B;
    }

    int main()
    {
        cout << "Difference: " << sub2(25, 10);
        return 0;
    }

Since C++ is a top-down parsed language, it constructs a parse tree from the top and needs to know in advance about the functions before they are used. It is needed not define the function before it is called, but declare it.

Functions must be declared before their usage to avoid compilation errors. However, in a program with multiple functions that call each other or externally included files, these errors are hard to avoid, which is why forward declarations are used.

Forward Declaration of Classes in C++
**************************************

Forward declarations also exist for classes in C++.

.. code-block:: cpp
    :linenos:

    #include <iostream>
    using namespace std;

    //Forward declaration of classes One and Two
    class One;
    class Two;

    class One
    {
        int y;
        public:
            void num(int a)  //Getting input number
            {
                y = a;
            }
            friend int sub2(One, Two);
    };
    class Two
    {
        int x;
        public:
            void num(int a)  //Getting input number
            {
                x = a;
            }
            friend int sub2(One, Two);
    };
    int sub2(One a, Two b)  //Subtraction of two numbers from both classes
    {
        int ans = a.y - b.x;
        return ans;
    }

    int main()
    {
        Two y;
        One x;

        x.num(25);
        y.num(10);

        cout << "Difference: " << sub2(x,y);
        return 0;
    }

If classes are not declared before being used, the compiler generates an error too.

Why the C++ Compiler Needs Forward Declaration
***********************************************

The forward declaration is necessary as it helps the compiler ensure 3 things:

* The program is correct and has no token spelling mistakes.
* The arguments of the declared function are correct.
* The declared function exists in the program and is defined below.

If you did not forward declare the functions, the compiler would create an additional object file containing information with various guesses as to what your function might be.

And the linker (a program that links multiple objects and classes into a single executable object file) would have a linkage issue, as it might have an existing function of the same name but with arguments of a different data type.

For example, assume you have a function int sub2(int a, int b). Without the forward declaration, the linker might get confused with another existing function int sub2(float a, float b).

A compiler validates the code for a clean file with a C++ forward declaration. It would be best to remember that C++ might compile and run such a program in some cases.

However, it would not provide the expected output. This is why the compiler requires forward declarations before implementing or using them in your code.

Advantages of Using Forward Declaration in C++
***********************************************

Forward declarations help the compiler validate your code better and help avoid linkage issues. But it also helps:

* Avoid Namespace Polluting: Forward declarations help ensure no code snippet is misplaced and avoid polluting a namespace.

* Improve Compilation Time: You can add the declaration of a function into your C++ program by including a header file, and the compiler would parse all the tokens provided in the file, which can take a long time. However, you can avoid this lengthy processing and use forward declaration for the particular classes that you intend to use instead of the whole cpp file.

* This might not impact smaller codes but comes in handy in more significant projects as it can minimize compilation times, thereby reducing time complexity. So instead of including a whole C++ file, you can use a specific class with the .h extension.

* Avoid Name Collision: Forward declarations also help ensure there is no collision of token or preprocessor names in the program if there are different projects with matching function or class names.

* Break Cyclic Dependency: The forward declaration of a class can solve cyclic references by declaring the particular parts needed in a file and leaving the header out of it.

Avoid Circular Dependency Using Forward Declaration in C++
***********************************************************

Two classes related or using each other's functions create a circular relation. This is known as cyclic or circular dependency.

Suppose there are two classes within the program where both need to use the other. In that case, a header file will be added for one, but it will further try to include the header file for the other circularly dependent class, creating a cycle where each header tries to have the other one.
