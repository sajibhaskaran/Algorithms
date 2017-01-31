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

print(factorialize(10))
print(factorialize(0))
print(factor(10))
print(factor(0))
    
