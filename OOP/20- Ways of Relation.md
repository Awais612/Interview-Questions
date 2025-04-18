## Through how many ways classes can be related in OOP?
`Technosoft`
<br><br>

In Object-Oriented Programming (OOP), classes can be related in several fundamental ways, each serving a unique purpose in designing and organizing code. Here are the primary types of relationships between classes:
<br><br>



### Association:
This is a general relationship where two classes communicate with each other, but neither class owns the other.

##### Example
A `Student` class and a `Course` class have an association if a student can enroll in multiple courses.
<br><br>



### Aggregation:
A specialized form of association, where one class (the whole) contains references to other classes (parts), but the "parts" can exist independently of the "whole."

##### Example
A `Library` class aggregating `Books`. Books can exist outside of the library, but the library has a collection of books.
<br><br>



### Composition:
A stronger form of aggregation, where the "part" cannot exist independently of the "whole." If the "whole" is destroyed, so are its "parts."

##### Example
A `House` class and a `Room` class. Rooms do not exist without the house.
<br><br>



### Inheritance:
This defines a "is-a" relationship, where one class (the subclass) inherits properties and behaviors from another class (the superclass).

##### Example
A `Dog` class inheriting from an `Animal` class. Here, Dog is a specific type of Animal.
<br><br>



### Dependency:
A weaker relationship where one class depends on another to function or perform a certain task. Changes in one class might affect the dependent class.

##### Example
A `Car` class depends on a `Driver` class to operate it.
<br><br>


These relationships provide flexibility, modularity, and reusability in OOP, allowing developers to design systems that are organized and maintainable.



### 🔗 Class Relationship Types in OOP

| Relationship      | Type               | Description                                                  | Example                        |
|-------------------|--------------------|--------------------------------------------------------------|--------------------------------|
| **Inheritance**   | IS-A               | One class inherits from another                              | `Dog IS-A Animal`              |
| **Composition**   | HAS-A              | One class owns another class strongly                        | `Car HAS-A Engine`             |
| **Aggregation**   | HAS-A (weak)       | One class uses another, but not tightly bound                | `Department HAS-A Professor`   |
| **Association**   | Uses / Linked      | Classes are connected, but no ownership                      | `Teacher teaches Student`      |
| **Dependency**    | Uses-A             | Temporary, method-level relationship                         | `Order uses Payment`           |
| **Realization**   | Implements         | A class implements an interface                              | `Dog implements Pet`           |

