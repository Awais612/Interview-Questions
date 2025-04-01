# Runtime Polymorphism vs Compile-Time Polymorphism
`Frag Games`

Polymorphism is one of the key concepts in Object-Oriented Programming (OOP) and refers to the ability of different objects to be accessed through the same interface. However, polymorphism can be implemented in two distinct ways: **compile-time** and **runtime polymorphism**.

<br><br>

## Compile-Time Polymorphism

**Compile-time polymorphism** is also known as **static polymorphism**. It is resolved during the compilation of the program. The most common mechanisms to achieve compile-time polymorphism are:

- **Function Overloading:** Same function name with different parameter lists.
- **Operator Overloading:** Custom implementation of operators (like `+`, `-`, etc.) for user-defined data types.

### Key Characteristics

- **Early Binding:** The method call is resolved at compile time.
- **Performance:** Since binding is done at compile time, there is no extra overhead during execution.
- **Flexibility:** Limited to methods with different signatures; the decision is made by the compiler.

### Example: Function Overloading (C++)

```cpp
#include <iostream>
using namespace std;

class MathOperations {
public:
    // Function overloading: different parameter types
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
};

int main() {
    MathOperations math;
    cout << "Sum of integers: " << math.add(5, 10) << endl;
    cout << "Sum of doubles: " << math.add(5.5, 10.5) << endl;
    return 0;
}
```

**Explanation:**
- The `add` method is overloaded with two versions, one for integers and another for doubles.
- The compiler determines which version to call based on the argument types during compilation.

<br><br>

## Runtime Polymorphism

**Runtime polymorphism** is known as **dynamic polymorphism**. It is resolved during the execution of the program, primarily using inheritance and method overriding.

### Key Characteristics

- **Late Binding:** The method call is determined at runtime based on the actual object type.
- **Flexibility:** Allows the program to decide at runtime which method to call, making it possible to work with objects of different classes through a common interface.
- **Overhead:** Since binding is deferred until runtime, there is a slight performance overhead compared to compile-time polymorphism.

### Example: Method Overriding (C++)

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
    // Virtual function allows for runtime polymorphism
    virtual void sound() {
        cout << "Animal makes a sound" << endl;
    }
};

class Dog : public Animal {
public:
    // Overriding the base class method
    void sound() override {
        cout << "Dog barks" << endl;
    }
};

class Cat : public Animal {
public:
    // Overriding the base class method
    void sound() override {
        cout << "Cat meows" << endl;
    }
};

void makeSound(Animal* animal) {
    animal->sound();
}

int main() {
    Animal animal;
    Dog dog;
    Cat cat;
    
    // Demonstrating runtime polymorphism
    makeSound(&animal); // Outputs: Animal makes a sound
    makeSound(&dog);    // Outputs: Dog barks
    makeSound(&cat);    // Outputs: Cat meows
    
    return 0;
}
```

**Explanation:**
- The `Animal` class has a virtual function `sound()`.
- The derived classes (`Dog` and `Cat`) override this function.
- The decision of which `sound()` method to invoke is made at runtime based on the type of the object passed to the function `makeSound()`.

<br><br>

## Key Differences

| Aspect                      | Compile-Time Polymorphism         | Runtime Polymorphism                |
|-----------------------------|-----------------------------------|-------------------------------------|
| **Binding**                 | Early binding (compile time)      | Late binding (runtime)              |
| **Mechanisms**              | Function/Operator Overloading     | Virtual Functions, Method Overriding|
| **Performance**             | Faster (no runtime overhead)      | Slight overhead due to dynamic binding|
| **Flexibility**             | Less flexible (determined at compile time) | More flexible (can change behavior at runtime)|
| **Use Cases**               | When behavior is known in advance | When behavior should vary dynamically|

