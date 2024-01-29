Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. The four pillars of OOP are fundamental concepts that help structure and design software in a modular and efficient way. These four pillars are:

# Encapsulation
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

# Abstraction

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
