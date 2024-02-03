# Types of Inheritance

In Java, inheritance is a fundamental concept that allows a class to inherit properties and behaviors from another class. There are several types of inheritance in Java:

## 1- Single Inheritance:

- A class can inherit from only one superclass.
### Example:

```java
class Parent {
    // parent class code
}

class Child extends Parent {
    // child class code
}
```

## 2- Multiple Inheritance (through interfaces):
- Java doesn't support multiple inheritance of classes to avoid the "diamond problem," but it supports multiple inheritance through interfaces.

### Example:

```java
interface Interface1 {
    // interface code
}

interface Interface2 {
    // interface code
}

class MyClass implements Interface1, Interface2 {
    // class code
}
```

## 3- Multilevel Inheritance:
- A class can inherit from another class, and then another class can inherit from it, forming a chain of inheritance.

### Example:

``` java
class Grandparent {
    // grandparent class code
}

class Parent extends Grandparent {
    // parent class code
}

class Child extends Parent {
    // child class code
}
```

## 4- Hierarchical Inheritance:
- Multiple classes can inherit from a single superclass.

### Example:

```java
class Parent {
    // parent class code
}

class Child1 extends Parent {
    // child1 class code
}

class Child2 extends Parent {
    // child2 class code
}
```

## 5- Hybrid Inheritance:
- A combination of multiple types of inheritance in a single program.

### Example:

```java
class A {
    // class A code
}

class B extends A {
    // class B code
}

interface C {
    // interface C code
}

class D extends B implements C {
    // class D code
}
```