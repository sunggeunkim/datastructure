def divide(n,d):
    if d == 0:
        raise ValueError
    if n == 0:
        return "0"
    if n % d == 0:
        return str(n/d)
    sign = ""
    if n * d < 0:
        sign = "-"
        n = abs(n)
        d = abs(d)
    integer = n // d
    x = n - integer * d
    m = []
    while True:
        j = 1
        while x * (10**j) < d:
            m.append("0")
            j += 1
        rx = x * (10**j) // d
        strx = str(rx)
        x = x * (10**j) - rx * d
        if x == 0:
            m.append(strx)
            r = "".join(m)
            break
        found = False
        for i in range(len(m)):
            if strx == m[i]:
                start = i
                found = True
                break
        if found:
            r = "".join(m[:i]) + "[" + "".join(m[i:]) + "]"
            break
        else:
            m.append(strx)
    if len(r) == 1 and r == '0':
        return sign + str(integer)
    else:
        return sign + str(integer) + "." + r

print(divide(-50,6))
