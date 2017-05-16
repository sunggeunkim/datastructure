'''
Output numbers from 1 to x. If the number is divisible by 3, replace it with “Fizz”. If it is divisible by 5, replace it with “Buzz”. If it is divisible by 3 and 5 replace it with “FizzBuzz”.

reference: http://www.byte-by-byte.com/fizzbuzz/
'''
def FizzBuzz(x):
    for i in range(1, x+1):
        if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
        elif i % 3 == 0: print("Fizz")
        elif i % 5 == 0: print("Buzz")
        else: print(i)

FizzBuzz(15)

