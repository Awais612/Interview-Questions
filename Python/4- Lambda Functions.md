# What are lambda functions in python and how are they different from others when should we use it?

`Arbisoft`

Lambda functions in Python are <mark>small, anonymous</mark> functions defined using the `lambda` keyword. Unlike regular functions that are defined using the `def` keyword and can contain multiple expressions, lambda functions are limited to a single expression. Here's a basic structure of a lambda function:

```python
lambda arguments: expression
```
<br>

## Differences from Regular Functions:

### 1-  Syntax:
- <strong>Lambda Functions</strong>: Defined using `lambda` and can contain only a single expression. They do not require a return statement; the expression's result is returned automatically.
- <strong>Regular Functions</strong>: Defined using `def` and can contain multiple expressions and statements. They require an explicit `return` statement to return a value.

```python
# Lambda function
square = lambda x: x ** 2

# Regular function
def square(x):
    return x ** 2
```

### 2-  Name:
- **Lambda Functions**: Anonymous (no name), though they can be assigned to a variable.
- **Regular Functions**: Named, which allows them to be referenced later.

### 3-  Scope:
- **Lambda Functions**: Typically used in places where a small, throwaway function is needed, like within higher-order functions (e.g., `map`, `filter`, `sorted`).
- **Regular Functions**: Used for more complex operations that require more than one line of code or need to be reused.

### 4-  Readability:
- **Lambda Functions**: Can be harder to read, especially for complex logic, due to their concise syntax.
- **Regular Functions**: More readable and maintainable for complex operations.
<br><br>

## When to Use Lambda Functions:
- **Single-use, simple functions**: Lambda functions are perfect for situations where you need a small function temporarily and don't want to formally define it using `def`.
- **Higher-order functions**: They are commonly used with functions like `map, filter, and sorted`, where you need to pass a function as an argument.

```python
# Example with map
numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16]

# Example with filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# Example with sorted
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs_sorted = sorted(pairs, key=lambda pair: pair[1])
print(pairs_sorted)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

- **Inline small operations**: When you want to perform a small operation inline, particularly within other functions or methods, without cluttering your code with full function definitions.
<br><br>

## When Not to Use Lambda Functions:
- **Complex logic**: If the function logic is complex or you plan to reuse it, a regular function is preferable for readability and maintainability.
- **Documentation**: Regular functions can have docstrings, making them easier to document and understand, while lambda functions cannot.


Lambda functions are best suited for small, simple operations where defining a full function would be unnecessary. However, for anything more complex or where code clarity is a priority, regular functions are a better choice.