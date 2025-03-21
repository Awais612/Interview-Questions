# What are the key differences between interfaces and abstract classes in object-oriented programming, and when should one be preferred over the other?
`Netsol` `Dynamic Solutions` `Frag Games`

In object-oriented programming (OOP), interfaces and abstract classes are both used to define common behavior that can be shared among different classes. However, there are some key differences between them.

## Abstract Class

### Definition
- An abstract class is a class that cannot be instantiated on its own. It serves as a `blueprint` for other classes.
- It can have both abstract (unimplemented) and concrete (implemented) methods.
- Abstract classes can also have instance variables.

### Inheritance:
- A class can inherit from only one abstract class.
- Abstract classes support the concept of code reusability through inheritance.

### Constructor:
- Abstract classes can have constructors, and they are usually invoked when an instance of a derived class is created.

### Access Modifiers:
- Abstract classes can have access modifiers for their methods and variables.
___
<br><br>

## Interface

### Definition:
- An interface is a collection of abstract methods. It provides a contract for classes that implement it.
- Interfaces cannot have instance variables or concrete methods (until Java 8, which introduced default and static methods in interfaces).

### Inheritance:
- A class can implement multiple interfaces.
- Interfaces support multiple inheritances, allowing a class to inherit behavior from multiple sources.

### Constructor:
- Interfaces cannot have constructors because they cannot be instantiated.

### Access Modifiers:
- All methods in an interface are implicitly public and abstract (prior to Java 8). With Java 8, default and static methods can have access modifiers.
___
<br><br>


## Commonalities:

### Abstraction:
Both abstract classes and interfaces provide a level of abstraction, allowing you to define a common set of methods without specifying the implementation details.

### Polymorphism:
Both support polymorphism, enabling objects of different classes to be treated as objects of a common type.

## When to Use Which:

### Abstract Class:
- Use when you want to provide a common base class with some shared implementation.
- If you need to use constructors in your design.
- When a class should inherit from only one base class.

### Interface:
- Use when you want to define a contract for multiple classes to implement.
- When you need to support multiple inheritances.
- If you want to provide a common set of methods without specifying the implementation.