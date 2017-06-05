def closestLocation(address, objects, names):
    close = 1e8
    address = address.lower()
    n = len(address)
    close_name = names[0]
    for i, name in enumerate(names):
        name_o = name
        name = name.lower()
        m = len(name)
        if m < n - 1:
            continue
        j = 0
        k = 0
        mismatch = 0
        while j < n:
            if address[j] != name[k]:                
                mismatch += 1
                if mismatch > 1:
                    break
                if j+1!=n and address[j+1]==name[k]:
                    j += 1
                elif k+1!=m and address[j]==name[k+1]:
                    k += 1
                elif k+1!=m and j+1!=n and\
                    address[j+1]==name[k+1]:
                    j += 1
                    k += 1
            j += 1
            k += 1
        if j == n or (j == n-1 and mismatch==0):
            d = calc_distance(objects[i])
            if d < close:
                close = d
                close_name = name_o
    return close_name

def calc_distance(x):
    if len(x) == 2:
        return x[0]**2 + x[1]**2
    if len(x) == 4:
        x1, y1 = x[0], x[1]
        x2, y2 = x[2], x[3]
        if x1 == x2:
            if y1 * y2 < 0:
                return x1 * x1
            else:
                return min(x1*x1+y1*y1, x2*x2+y2*y2)
        if y1 == y2:
            if x1 * x2 < 0:
                return y1 * y1
            else:
                return min(x1*x1+y1*y1, x2*x2+y2*y2)

