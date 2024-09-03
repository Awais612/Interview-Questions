# Difference between var and let in context of scoping
`Arbisoft`

In JavaScript, both `var` and `let` are used for variable declaration, but they have some key differences, particularly in terms of scoping.

## Scoping
- `var` is function-scoped, meaning that the variable is only visible within the function in which it is declared. If it is declared outside any function, it becomes a global variable.
- `let` is block-scoped, meaning that the variable is limited to the block, statement, or expression in which it is declared. Blocks include if statements, loops, and other structures denoted by curly braces '{}'

## Hoisting
- Variables declared with `var` are hoisted to the top of their scope during the compilation phase. This means you can use a variable before it is declared in the code. However, the value assigned to the variable will not be hoisted, only the declaration.
- Variables declared with `let` are also hoisted, but they are not initialized until the interpreter reaches the declaration. This means you cannot access the variable before the line where it is declared.

## Example
```javascript
// Using var
function exampleVar() {
  if (true) {
    var x = 10;
    console.log(x); // Outputs 10
  }
  console.log(x); // Outputs 10 (var is function-scoped)
}

// Using let
function exampleLet() {
  if (true) {
    let y = 20;
    console.log(y); // Outputs 20
  }
  // console.log(y); // Error: y is not defined (let is block-scoped)
}
```

In modern JavaScript development, it's generally recommended to use `let` and `const` over `var` because they provide more predictable scoping behavior and help avoid common issues associated with the hoisting of var variables. Additionally, const is used for variables that should not be re-assigned, providing a form of immutability.