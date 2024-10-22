# Final Keyword in OOP

`Netsol`
<br><br>

The final keyword in Object-Oriented Programming (OOP), particularly in Java, serves as a non-access modifier that restricts the modification of classes, methods, and variables. Its primary purpose is to enforce immutability and prevent unintended alterations in the code structure.

## Contexts of the Final Keyword

### 1- Final Variables
A variable declared as final can only be assigned once. After initialization, its value cannot be changed. This is particularly useful for defining constants.

```java
final int MAX_USERS = 10;
```

Attempting to reassign this variable will result in a compilation error.
<br><br>

### 2- Final Methods
Declaring a method as final prevents it from being overridden by subclasses. This ensures that the method's implementation remains consistent across the inheritance hierarchy.

```java
final void display() {
    System.out.println("This method cannot be overridden.");
}
```
<br><br>

### 3- Final Classes
A class marked as final cannot be subclassed. This is useful for creating immutable classes or for security reasons, ensuring that the class's behavior is not altered through inheritance.

```java
final class ImmutableClass {
    // Class implementation
}
```
<br><br>

## Characteristics and Benefits

- `Immutability`: The final keyword ensures that once a variable, method, or class is defined, it cannot be modified or extended further.
- `Performance Optimization`: The Java compiler can optimize code more effectively when it knows certain entities will not change.
- `Security`: By preventing modifications, the final keyword enhances security by safeguarding critical methods and data from being altered by subclasses or external classes.
- `Code Clarity`: Using final helps make the codebase clearer and easier to understand, as it explicitly indicates which parts of the code are intended to remain unchanged.

In summary, the final keyword is a crucial tool in Java OOP that aids in maintaining control over class behavior and ensuring data integrity throughout the application lifecycle