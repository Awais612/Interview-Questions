# Print all the divisors of the number

```pseudocode
def printDivisors():
    divisors = []
    for(int i=0; i<sqrt(n); i++):
        if(n % i == 0):
            divisors.add(i)
        
        if(n / i != i):
            divisors.add(n/i)

    divisors.sort()
    return divisors
```

> It's time complexity is `O(sqrt(n))`

### Common Problems
- GCD / HCF
- Prime numbers