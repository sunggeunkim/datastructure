import math

def isPrime(x):
    if x == None:
        return None
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(isPrime(13))
print(isPrime(124))
print(isPrime(997))
print(isPrime(961748941))
        
