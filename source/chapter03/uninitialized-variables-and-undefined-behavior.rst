###################################################
Uninitialized variables and undefined behavior
###################################################

Uninitialized variables
************************

Unlike some programming languages, C/C++ does not initialize most variables to a given value (such as zero) automatically. Thus when a variable is assigned a memory location by the compiler, the default value of that variable is whatever (garbage) value happens to already be in that memory location! A variable that has not been given a known value (usually through initialization or assignment) is called an **uninitialized variable**.

To recap:

* **Initialization**: The object is given a known value at the point of definition.
* **Assignment**: The object is given a known value beyond the point of definition.
* **Uninitialized**: The object has not been given a known value yet.

Using the values of uninitialized variables can lead to unexpected results.

Most modern compilers will attempt to detect if a variable is being used without being given a value. If they are able to detect this, they will generally issue a compile-time error.

Undefined behavior
************************

**Undefined behavior** is the result of executing code whose behavior is not well defined by the C++ language. In this case, the C++ language does not have any rules determining what happens if the value of a variable is used before been given a known value.

Code implementing undefined behavior may exhibit any of the following symptoms:

* The program produces different results every time it is run.
* The program consistently produces the same incorrect result.
* The program behaves inconsistently (sometimes produces the correct result, sometimes not).
* The program seems like its working but produces incorrect results later in the program.
* The program crashes, either immediately or later.
* The program works on some compilers but not others.
* The program works until some other seemingly unrelated code is changed.

Or, the code may actually produce the correct behavior anyway. The nature of undefined behavior is that it is never quite known what result is going to generate.
