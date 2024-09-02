# Overloading vs Overriding
`Tintash` `Arbisoft`

### Overloading: 
Overloading refers to defining multiple methods in a class with the same name but different parameters. These methods can have different implementations or functionalities.

### Overriding: 
Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass has the same name, same parameters, and same return type as the method in the superclass.
<br><br>

## Examples
Here are some real-time examples to illustrate both concepts:


### Overloading Example:

```java
public class Calculator {
    // Method to add two integers
    public int add(int a, int b) {
        return a + b;
    }

    // Overloaded method to add three integers
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Overloaded method to add two doubles
    public double add(double a, double b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(2, 3)); // Outputs: 5
        System.out.println(calc.add(2, 3, 4)); // Outputs: 9
        System.out.println(calc.add(2.5, 3.5)); // Outputs: 6.0
    }
}
```

In this example, the **Calculator** class demonstrates method overloading by providing multiple `add()` methods with different parameter lists.

### Overriding Example:

Let's consider a simplified banking system. We have a **BankAccount** superclass and subclasses for different types of accounts such as `SavingsAccount` and `CheckingAccount`. Each type of account might have specific rules for calculating interest or fees. We'll focus on the method `calculateInterest()` which is overridden in subclasses.

```java
// Superclass
class BankAccount {
    protected double balance;

    // Constructor
    public BankAccount(double balance) {
        this.balance = balance;
    }

    // Method to calculate interest
    public double calculateInterest() {
        // Default implementation: 0% interest
        return 0.0;
    }
}

// Subclass for savings account
class SavingsAccount extends BankAccount {
    // Constructor
    public SavingsAccount(double balance) {
        super(balance);
    }

    // Overrides calculateInterest() method for savings account
    @Override
    public double calculateInterest() {
        // Simplified interest calculation for savings account
        return balance * 0.05; // 5% annual interest
    }
}

// Subclass for checking account
class CheckingAccount extends BankAccount {
    // Constructor
    public CheckingAccount(double balance) {
        super(balance);
    }

    // Overrides calculateInterest() method for checking account
    @Override
    public double calculateInterest() {
        // Checking account typically doesn't offer interest
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating instances of different types of accounts
        BankAccount savingsAccount = new SavingsAccount(1000.0);
        BankAccount checkingAccount = new CheckingAccount(2000.0);
        
        // Calculating interest for each account
        double savingsInterest = savingsAccount.calculateInterest();
        double checkingInterest = checkingAccount.calculateInterest();
        
        // Outputting results
        System.out.println("Interest for savings account: " + savingsInterest); // Outputs: 50.0
        System.out.println("Interest for checking account: " + checkingInterest); // Outputs: 0.0
    }
}

```
