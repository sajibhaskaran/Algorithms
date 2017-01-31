# Purpose: Factorialize a Number
#          Return the factorial of the provided integer.
# Author : Saji Bhaskaran


def factorialize(number):
    result = 1
    if number == 0:
        return result
    else:
        for i in range(1,number+1):
            result *= i
    return result

# Refactored...

def factor(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Another version

def fact(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return (n * fact(n-1))
    

print(factorialize(10))
print(factorialize(0))
print(factor(10))
print(factor(0))
print(fact(10))
print(fact(-1))
    
