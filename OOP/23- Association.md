## Association (Example in real life + Code Implementation)
`Technosoft`
<br><br>

**Association** is a relationship between two classes that establishes a connection without implying ownership. This connection allows objects of one class to use objects of another, but each class can still function independently. Association is commonly found in real-life scenarios where there is a logical relationship between two entities.
<br><br>

## Real-Life Example

A **teacher** and a **student** are associated because a teacher can teach multiple students, and a student can learn from multiple teachers. However, a teacher doesn’t own a student, nor does a student own a teacher. They simply share a relationship based on a common activity (teaching and learning).
<br><br>

## Code Implementation

Here’s how you might represent this association in code using Python:

```python
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []  # List to hold associated Student objects

    def add_student(self, student):
        self.students.append(student)
        print(f"{self.name} is now teaching {student.name}")

class Student:
    def __init__(self, name):
        self.name = name

# Creating instances of Teacher and Student
teacher1 = Teacher("Abdullah")
student1 = Student("Yaqub")
student2 = Student("Uppal")

# Associating teacher with students
teacher1.add_student(student1)
teacher1.add_student(student2)

# Output:
# Abdullah is now teaching Yaqub
# Abdullah is now teaching Uppal
```
<br><br>

In this example:
- **Association** is demonstrated by the Teacher class holding a list of Student objects.
- There’s no ownership or lifecycle dependency between Teacher and Student.