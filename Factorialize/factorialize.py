


def factorialize(number):
    result = 1
    if number == 0:
        result = 1
    else:
        for i in range(1,number+1):
            result *= i
    return result

print(factorialize(15))
    
