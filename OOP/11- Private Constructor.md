# Can We Make Constructor Private, How Will We Make Object of Such Class

Yes, you can make a constructor private in a class. This is often done to enforce certain restrictions on object creation or to implement design patterns like the Singleton pattern. If a constructor is private, it cannot be directly invoked from outside the class.

To make a constructor private, you can simply declare it with the `private` access modifier. Here's an example in Java:

```java
public class MyClass {
    private static MyClass instance;  // Assuming you want to implement a Singleton pattern
    
    private MyClass() {
        // Private constructor
    }

    public static MyClass getInstance() {
        if (instance == null) {
            instance = new MyClass();
        }
        return instance;
    }

    // Other methods and properties of the class
}
```

In this example, the constructor `MyClass()` is private, and an instance of the class can only be obtained through the `getInstance()` method, which ensures that only one instance is created (Singleton pattern).