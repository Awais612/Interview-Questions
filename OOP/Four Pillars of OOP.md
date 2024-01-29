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