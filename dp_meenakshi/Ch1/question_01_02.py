def array_sum(arr, i):
    if i == 0: return arr[0]
    arr[i] += array_sum(arr, i-1)
    return arr[i]

a = [1,2,3,4,5,6]
array_sum(a, 5)
print(a)
