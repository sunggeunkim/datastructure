'''
reference: https://codefights.com/interview-practice/task/oJXTWuwEZiC6FTw3A

You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

Example

For n = 1, the output should be
climbingStairs(n) = 1;

For n = 2, the output should be
climbingStairs(n) = 2.

You can either climb 2 steps at once or climb 1 step two times.

Input/Output

[time limit] 4000ms (py3)
[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 50.

[output] integer

It's guaranteed that the answer will fit in a 32-bit integer.
'''

def climbingStairs(n):
    if n == 0 or n == 1:
        return n

    f = [0] * n
    f[0] = 1
    f[1] = 2
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
        
    return f[-1]
    
