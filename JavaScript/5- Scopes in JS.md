# Scopes in JavaScript
`Arbisoft`

In JavaScript, scope refers to the region of a program where a particular variable can be accessed or modified. There are two main types of scope in JavaScript: local scope and global scope.

## 1- Local Scope

- Variables declared inside a function have local scope, meaning they are only accessible within that function.
- Parameters of a function also have local scope.
- Variables declared using the let or const keyword inside a block (if statement, loop, etc.) have block scope and are only accessible within that block.

Example of local scope:

```javascript
function exampleFunction() {
  let localVar = 'I am local';
  console.log(localVar);
}

exampleFunction(); // Output: I am local
console.log(localVar); // Error: localVar is not defined
```

## 2- Global Scope

- Variables declared outside of any function or block have global scope and can be accessed from anywhere in the code.
- Variables declared without using `let`, `const`, or `var` automatically become global variables.

Example of global scope:

```javascript
let globalVar = 'I am global';

function exampleFunction() {
  console.log(globalVar);
}

exampleFunction(); // Output: I am global
console.log(globalVar); // Output: I am global
```

It's important to note that when a variable is declared inside a function without using let, const, or var, it becomes a global variable. However, using let or const inside a function will limit the variable's scope to that function.

Understanding and managing scope is crucial for avoiding unintended side effects and maintaining clean and organized code. Local scope helps encapsulate variables, preventing them from affecting the rest of the program, while global scope allows for broader accessibility when needed.