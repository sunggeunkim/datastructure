'''
Write a function that returns all permutations of a given list.

permutations({1, 2, 3})
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def string_permutations(s):
    results = [] 
    string_permutation("", s, results)
    return results

def string_permutation(prefix, suffix, results):
    if len(suffix) == 0:
        results.append(prefix)
    else:
        for i in range(0, len(suffix)):
            string_permutation(prefix + suffix[i], suffix[:i] + suffix[i+1:], results)

def list_permutations(a, start, results):
    if start >= len(a):
        results.append(list(a))
    else:
        for i in range(start, len(a)):
            swap(a, start, i)
            list_permutations(a, start+1, results)
            swap(a, start, i)

a = "abc"
print(string_permutations(a))
    
a = [1, 2, 3]
results = []
list_permutations(a, 0, results)
print(results)
