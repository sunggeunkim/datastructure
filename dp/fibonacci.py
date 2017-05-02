def fib_recur(n):
    if n < 2:
        return n
    return fib_recur(n-1) + fib_recur(n-2)

def fib_iter(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a+b
    return a

print(fib_recur(10))
print(fib_iter(10))
