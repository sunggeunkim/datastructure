def math_table_rec(n, i):
    if i == 0:
        return
    print(n, " * ", i, " = ", n * i)
    math_table_rec(n, i-1)

math_table_rec(8, 10)
