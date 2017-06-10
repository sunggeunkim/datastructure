'''
A happy number is a number defined by the following process: 
Start with any positive integer and replace the number with 
the sum of the squares of its digits. Repeat this process 
until the number equals 1, at which point it will stay 1, 
or it loops endlessly in a cycle that does not include 1. 
A number for which this process ends in 1 is happy.
'''

def happyNumber(n):
    x = set()
    while n not in x:
        x.add(n)
        nstr = str(n)
        n = sum([int(i)**2 for i in nstr])
    if n == 1:
        return True
    else:
        return False
