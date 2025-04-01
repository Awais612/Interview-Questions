# The Diamond Problem
`Frag Games`

The **Diamond Problem** occurs in multiple inheritance when two classes inherit from the same superclass, and a further class inherits from both of these classes. This creates an inheritance "diamond" shape. The main issue arises when a method in the top-level superclass is inherited by both intermediate classes. When the bottom-level class calls that method, the interpreter must decide which superclass method to invoke.

<br><br>

## Visual Representation of the Diamond Problem

```
     A
    / \
   B   C
    \ /
     D
```

- **A**: The top-level base class.
- **B** and **C**: Two classes that inherit from **A**.
- **D**: The class that inherits from both **B** and **C**.

<br><br>

## Example in Python

Let’s look at an example to see the diamond problem in action and how Python resolves it.

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

# Create an instance of D and call greet()
d = D()
d.greet()

# Print the Method Resolution Order for class D (Optional)
print("MRO for class D:", [cls.__name__ for cls in D.mro()])
```
<br><br>

### Explanation:
1. **Class Definitions:**
   - **A**: Base class with a simple `greet()` method.
   - **B** and **C**: Both override the `greet()` method and then call `super().greet()`. This ensures that the next method in the MRO is called.
   - **D**: Inherits from both **B** and **C** and further overrides `greet()`, again using `super()` to call the next method in line.

2. **Method Call Flow:**
   - When `d.greet()` is called:
     - The call starts in **D**.
     - Then, using `super()`, Python follows the MRO, which typically is `[D, B, C, A, object]`.
     - **D** calls **B**'s `greet()`, which prints "Hello from B" and then calls `super().greet()`.
     - The next in line is **C**'s `greet()`, printing "Hello from C" and calling `super().greet()`.
     - Finally, **A**'s `greet()` is called, printing "Hello from A".

3. **MRO Inspection:**
   - The printed MRO shows the exact order in which Python resolves method calls for class **D**:
     ```python
     MRO for class D: ['D', 'B', 'C', 'A', 'object']
     ```



<br><br>

## How Python Resolves the Diamond Problem (Optional)

Python uses the **C3 Linearization Algorithm** to determine the **Method Resolution Order (MRO)**. This algorithm provides a consistent order in which base classes are searched when executing a method. In Python, you can inspect the MRO using the `mro()` method or the `__mro__` attribute.

### Key Points:
- **Consistency:** Python’s MRO ensures a consistent order regardless of the complexity of the inheritance graph.
- **Super() Function:** When using `super()`, Python follows the MRO to decide which method to call next, which is particularly useful in diamond inheritance scenarios.