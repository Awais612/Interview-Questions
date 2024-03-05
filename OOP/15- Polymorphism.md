# Polymorphism
`Arbisoft` `Dynamic Solutions`

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different types to be treated as objects of a common base type. The term "polymorphism" is derived from Greek, meaning "many forms." It enables a single interface to represent various types and is often associated with two main types: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.

## Compile-time Polymorphism

- Also known as static polymorphism or method overloading.
- Occurs during the compilation phase.
- Involves multiple methods with the same name in the same class, but with different parameter types or a different number of parameters.
- The correct method is determined at compile time based on the method signature.

```java
public class Example {
    // Method Overloading
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }
}
```

## Runtime Polymorphism

- Also known as dynamic polymorphism or method overriding.
- Occurs during runtime.
- Involves a base class and a derived class, where the derived class provides a specific implementation of a method defined in the base class.
- The correct method is determined at runtime based on the actual type of the object.

```java
// Base class
class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Derived class
class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

```java
// Using runtime polymorphism
Animal myAnimal = new Dog();
myAnimal.sound();  // Calls Dog's implementation of sound()
```

Polymorphism promotes code reusability, flexibility, and the ability to work with objects at a higher level of abstraction. It is a key principle in OOP and is often linked with encapsulation and inheritance to create more modular and maintainable code.
