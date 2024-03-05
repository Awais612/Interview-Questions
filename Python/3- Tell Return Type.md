# How to Explicitly mention return type in python
`Arbisoft`

In Python, the return type of a function is not explicitly declared like in some other programming languages. Python is dynamically typed, meaning you don't need to specify the return type when defining a function. The interpreter infers the return type based on the values returned by the function.

However, you can use `type hints` to provide information about the expected types in function signatures. Type hints are optional and don't affect the actual runtime behavior of the code, but they can be helpful for documentation and tools like linters or type checkers.

Here's an example of using type hints for a function:

```python
def add_numbers(a: int, b: int) -> int:
    result = a + b
    return result
```

In this example, a and b are expected to be integers, and the function is expected to return an integer. The syntax `-> int` after the parentheses indicates the expected return type.

Keep in mind that type hints are not enforced by the Python interpreter itself. They are more of a documentation tool and can be used by external tools like MyPy for static type checking.

If you want to check the type of a value during runtime, you can use the `type()` function or the `isinstance()` function. Here's an example:

```python
result = add_numbers(3, 4)
print(type(result))  # Output: <class 'int'>
```

In this case, `type(result)` will return the type of the value stored in the result variable, confirming that it's an integer.