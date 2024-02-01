# Why do we use & in Copy Ctr parameters list?

In the context of a copy constructor in C++, the & symbol is used to denote a reference. The copy constructor is a special constructor in a class that creates an object by copying the members of another object of the same class. The & symbol in the parameter list indicates that the parameter is a reference to an object, rather than a direct copy.

Here's an example of a copy constructor in C++:

```cpp
#include <iostream>

class MyClass {
    public:
        // Constructor
        MyClass(int value) : data(value) {
            std::cout << "Constructor called with value: " << data << std::endl;
        }

        // Copy constructor
        MyClass(const MyClass &source) : data(source.data) {
            std::cout << "Copy constructor called. Copied value: " << data << std::endl;
        }

        // Member function
        void display() {
            std::cout << "Data: " << data << std::endl;
        }
    private:
        int data;
};

int main() {
    // Create an object using the constructor
    MyClass obj1(42);

    // Use the copy constructor to create another object by copying the first one
    MyClass obj2 = obj1;

    // Display the data in both objects
    std::cout << "Object 1:" << std::endl;
    obj1.display();

    std::cout << "Object 2:" << std::endl;
    obj2.display();

    return 0;
}

```


This code defines a MyClass with a constructor that initializes an integer data and a copy constructor that creates a new object by copying the data from an existing object. The main function demonstrates creating objects and using the copy constructor to make a copy.


### Output of This Program

```
Constructor called with value: 42
Copy constructor called. Copied value: 42
Object 1:
Data: 42
Object 2:
Data: 42
```
