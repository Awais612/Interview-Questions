# How to Pass by Reference in Java

In Java, all arguments are passed by value. However, when you pass an `object as an argument`, you are actually passing the value of the reference to the object, not the object itself. This can sometimes be confusing, leading people to think of it as `pass by reference`.

To achieve a similar effect to pass by reference in Java, you can pass an object and modify its state within the method. Here's an example:

```java
class MyClass {
    int value;

    MyClass(int value) {
        this.value = value;
    }
}

public class PassByReferenceExample {
    public static void modifyValue(MyClass obj) {
        obj.value = obj.value * 2;
    }

    public static void main(String[] args) {
        MyClass myObject = new MyClass(5);
        System.out.println("Before: " + myObject.value);

        modifyValue(myObject);

        System.out.println("After: " + myObject.value);
    }
}
```

In this example, the modifyValue method takes an object of type MyClass as a parameter. Even though Java is technically passing the reference to myObject by value, any modifications made to the object's state inside the modifyValue method will affect the original object outside the method.

This behavior is possible because objects in Java are references, and when you pass an object reference, you are passing a copy of that reference, not the object itself. Thus, changes to the object's state inside the method are reflected in the original object.

It's important to note that `primitive types` (e.g., int, float, char) in Java are `passed by value`, and modifications to them inside a method will not affect the original value outside the method.