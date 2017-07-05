'''
ref: https://codefights.com/interview-practice/task/7o2Aba2Zep3MJPKQ3/description

A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent and you need to determine the total number of ways that the message can be decoded.

Since the answer could be very large, take it modulo 109 + 7.

Example

For message = "123", the output should be

mapDecoding(message) = 3.

"123" can be decoded as "ABC" (1 2 3), "LC" (12 3) or "AW" (1 23), so the total number of ways is 3.
'''

def mapDecoding(digits):
    if len(digits) == 0:
        return 1
    n = len(digits)
    count = [0] * (n+1)
    count[0] = 1
    count[1] = 1 if int(digits[0]) >= 1 else 0
    if len(digits) == 1:
        return count[1] 
    for i in range(2,n+1):
        if (int(digits[i-1]) > 0):
            count[i] = count[i-1]         
        if (0 < int(digits[i-2]) < 2 or (digits[i-2] == '2' and int(digits[i-1]) < 7)):
            count[i] += count[i-2]            
        count[i] = count[i] % (10**9 + 7)        
    return count[n]
