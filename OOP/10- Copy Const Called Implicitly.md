# Where is Copy Constructor Called Implicitly

In object-oriented programming languages like C++, a copy constructor is called implicitly in several situations. Here are some scenarios where the copy constructor is called implicitly:

### Passing objects by value:

When you pass an object to a function by value, a copy of the object is created, and the copy constructor is called to initialize the new object with the values of the passed object.

```cpp
void myFunction(MyClass obj) {
    // Copy constructor is called here
    // obj is a copy of the passed object
}

MyClass originalObject;
myFunction(originalObject);
```

###  Returning objects by value:

When a function returns an object by value, a copy of the local object is created to hold the return value, and the copy constructor is invoked.

```cpp
MyClass myFunction() {
    MyClass obj;
    // Some operations on obj
    return obj;  // Copy constructor is called to create a copy for the return value
}

MyClass newObj = myFunction();
```

### Creating a new object based on an existing object:

When you initialize a new object using an existing object, the copy constructor is called.

```cpp
MyClass originalObject;
MyClass newObj = originalObject;  // Copy constructor is called here
```

### Passing objects by value in a function return statement:

When you return an object by value in a function return statement, the copy constructor is called.

```cpp
MyClass createObject() {
    MyClass obj;
    // Initialize obj
    return obj;  // Copy constructor is called to return a copy of obj
}
```

