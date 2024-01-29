# Four Pillars of OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. The four pillars of OOP are fundamental concepts that help structure and design software in a modular and efficient way. These four pillars are:

## Encapsulation
**Definition:** Encapsulation is the bundling of data (attributes or properties) and the methods (functions or procedures) that operate on the data into a single unit, known as a class. It helps in hiding the internal details of an object and only exposing the necessary functionality.

**Example:**
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 5

my_car = Car("Toyota", "Camry")
my_car.accelerate()
print(my_car.speed)  # Output: 10
```

## Abstraction

**Definition:**
Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors they share, while ignoring irrelevant details. It allows programmers to focus on the relevant aspects of an object and hide unnecessary complexities.

**Example:**
```java
abstract class Shape {
    abstract double area();
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}

class Square extends Shape {
    private double sideLength;

    public Square(double sideLength) {
        this.sideLength = sideLength;
    }

    @Override
    double area() {
        return sideLength * sideLength;
    }
}

```

## Inheritancne

**Definition:**
Inheritance is a mechanism that allows a new class (subclass or derived class) to inherit properties and behaviors from an existing class (superclass or base class). This promotes code reuse and establishes a relationship between classes.

**Example:**
```java
class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public void speak() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println("Woof!");
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println("Meow!");
    }

```

## Polymorphism

**Definition:** 
Polymorphism allows objects of different types to be treated as objects of a common type. It enables a single interface to represent different types of objects, making code more flexible and extensible.

**Example:**

```java
class Bird {
    public void fly() {
        System.out.println("Bird is flying");
    }
}

class Sparrow extends Bird {
    @Override
    public void fly() {
        System.out.println("Sparrow can fly");
    }
}

class Penguin extends Bird {
    @Override
    public void fly() {
        System.out.println("Penguin can't fly");
    }
}

public class Main {
    public static void makeBirdFly(Bird bird) {
        bird.fly();
    }

    public static void main(String[] args) {
        Sparrow sparrow = new Sparrow();
        Penguin penguin = new Penguin();

        makeBirdFly(sparrow);  // Output: Sparrow can fly
        makeBirdFly(penguin);  // Output: Penguin can't fly
    }
}

```
