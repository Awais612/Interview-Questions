## Composition (Example in real life + Code Implementation)
`Technosoft`
<br><br>


**Composition** is a "strong has-a" relationship in which one class contains another class as a part, but this part cannot exist independently. If the "whole" object is destroyed, the "part" objects are also destroyed.
<br><br>


## Real-Life Example
A **car and its engine** represent a composition relationship. A car "has an" engine, but an engine is integral to the car's existence. If the car is destroyed, the engine typically goes along with it.
<br><br>


## Code Implementation in Python

Let's implement this using a `Car` class and an `Engine` class:

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine with horsepower", self.horsepower, "is starting...")

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        # Composition: Car "has an" Engine, created within the Car object itself
        self.engine = Engine(horsepower)

    def start_car(self):
        print(f"{self.model} is starting.")
        self.engine.start()

# Creating a Car object with a composed Engine object
my_car = Car("Tesla Model S", 670)
my_car.start_car()
```
<br><br>


## Explanation
1. The `Engine` class defines an engine with a horsepower attribute and a `start` method.
2. The `Car` class has an `Engine` as part of its structure, instantiated directly within the Car object. This means the engine is tightly coupled with the car.
3. The `start_car` method in `Car` calls the `start` method of its `Engine` object.
<br><br>


## Output
```
Tesla Model S is starting.
Engine with horsepower 670 is starting...
```
<br>

In this example, if the Car object is destroyed, the Engine instance contained within it is also destroyed, illustrating the "whole-part" relationship in composition. The Engine cannot exist independently of the Car in this scenario.
