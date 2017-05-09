def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def permutations(a, start, results):
    if start >= len(a):
        results.append(list(a))
    else:
        for i in range(start, len(a)):
            swap(a, start, i)
            permutations(a, start + 1, results)
            swap(a, start, i)

a = [1, 2, 3]
results = []
permutations(a, 0, results)
print(results)
