# Inheritance (Super vs SubClass)
`Arbisoft`

In object-oriented programming, inheritance is a mechanism that allows one class to inherit the properties and behaviors of another class. The class that is being inherited from is called the superclass or parent class, and the class that inherits from it is called the subclass or child class.

Here's a brief overview of how inheritance works, along with the concepts of superclass and subclass:

## Superclass (Parent Class)

- The superclass is the class that is being inherited from.
- It contains common properties and behaviors that can be shared by multiple subclasses.
- It serves as a template for creating more specialized subclasses.
- Inheritance allows the subclass to reuse and extend the functionality of the superclass.

## Subclass (Child Class)

- The subclass is the class that inherits from the superclass.
- It can have its own additional properties and behaviors.
- It has access to all the attributes and methods of the superclass and can override or extend them.

## super in Subclass

- The super is used in a subclass to call a method from its superclass.
- It is often used when you override a method in the subclass and still want to use the functionality of the overridden method in the superclass.

Let's create a simple example in Java to demonstrate inheritance with a superclass and two subclasses:

```java
// Superclass
class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public void speak() {
        System.out.println("Animal speaks");
    }

    public String getName() {
        return name;
    }
}

// Subclass 1
class Dog extends Animal {
    public Dog(String name) {
        super(name); // Call the constructor of the superclass
    }

    @Override
    public void speak() {
        System.out.println("Dog barks");
    }

    public void fetch() {
        System.out.println("Dog fetches");
    }
}

// Subclass 2
class Cat extends Animal {
    public Cat(String name) {
        super(name); // Call the constructor of the superclass
    }

    @Override
    public void speak() {
        super.speak(); // Call the speak method from the Animal superclass
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog("Buddy");
        Cat myCat = new Cat("Whiskers");

        System.out.println(myDog.getName() + " says:");
        myDog.speak();
        myDog.fetch();

        System.out.println("\n" + myCat.getName() + " says:");
        myCat.speak();
    }
}
```


