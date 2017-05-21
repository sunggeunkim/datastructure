'''
Find pairs in an integer array whose sum is equal to 10
 (bonus: do it in linear time)
'''

def find_pairs(a, n):
    s = set()
    for i in a:
        if n - i in s:
            return i, n-i
        else:
            s.add(i)

a = [1, 5, 3, 2, 6, 5, 10]

print(find_pairs(a, 10))
