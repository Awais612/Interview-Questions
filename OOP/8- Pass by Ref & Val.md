# Pass by Reference and Pass by Value
`Arbisoft`

"Pass by reference" and "pass by value" are terms used to describe how arguments are passed to functions in programming languages. These concepts are particularly relevant in languages that support both approaches, such as C++, Java, and others.

### Pass by Value

- In pass by value, the actual value of the argument is passed to the function.
- The function receives a copy of the argument's value, and any modifications made to the parameter inside the function do not affect the original variable outside the function.
- This is the default method of passing arguments in languages like C, Python, and others.

Example (in C++):
```cpp
void square(int x) {
    x = x * x;
}

int main() {
    int num = 5;
    square(num);
    // 'num' remains unchanged because 'num' was passed by value
}
```

### Pass by Reference

- In pass by reference, instead of passing the actual value, the memory address (reference) of the variable is passed to the function.
- This allows the function to directly access and modify the contents of the variable in the calling scope.
- In languages like C++ and some versions of Java, you can explicitly indicate that you want to pass a reference.

Example (in C++):

```cpp
void square(int &x) {
    x = x * x;
}

int main() {
    int num = 5;
    square(num);
    // 'num' is modified because 'num' was passed by reference
}
```

It's important to note that pass by reference can introduce potential side effects and makes the code less predictable, while pass by value is safer in terms of preserving the original state of variables. Each approach has its advantages and disadvantages, and the choice often depends on the specific requirements of the program and the desired behavior.