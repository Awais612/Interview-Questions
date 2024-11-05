## Aggregation (Example in Real Life + Code Implementation)
`Technosoft`
<br><br>


**Aggregation** represents a "has-a" relationship between objects, where one class (the whole) contains objects of another class (the parts). However, unlike composition, the parts can exist independently of the whole. Here’s a real-life example and a code implementation.
<br><br>


## Real-Life Example
Think of a **school and teachers**. A school has multiple teachers, but each teacher exists independently of the school. If the school closes, the teachers do not cease to exist; they can move to another school.
<br><br>


## Code Implementation in Python
Let's implement this using a `School` class and a `Teacher` class:

```python
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching.")

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []  # Aggregation: School "has" Teachers

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def conduct_classes(self):
        print(f"School {self.name} is conducting classes.")
        for teacher in self.teachers:
            teacher.teach()

# Creating Teacher objects
teacher1 = Teacher("Mr. Smith")
teacher2 = Teacher("Ms. Johnson")

# Creating School object and adding teachers to it
school = School("Greenwood High")
school.add_teacher(teacher1)
school.add_teacher(teacher2)

# Conduct classes at the school
school.conduct_classes()
```
<br><br>


## Explanation

1. The `Teacher` class defines a teacher with a name and a `teach` method.
2. The `School` class has a list of `Teacher` objects, representing an aggregation relationship.
3. The `add_teacher` method in `School` adds a teacher to the list of teachers, but the `Teacher` objects can exist independently of the `School`.
4. The `conduct_classes` method iterates over each teacher in the school and calls the `teach` method.
<br><br>


## Output

```
School Greenwood High is conducting classes.
Mr. Smith is teaching.
Ms. Johnson is teaching.
```
<br>

In this example, the School aggregates Teacher objects, but each Teacher can exist independently of the School. This reflects a real-life scenario where the existence of teachers doesn’t depend on the school they work at.
