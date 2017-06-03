def closestLocation(address, objects, names):
    close = 0
    n = len(address)
    for i, name in enumerate(names):
        m = len(name)
        if m < n - 1:
            continue
        j = 0
        k = 0
        mismatch = 0
        while j < n:
            if address[j] != name[k]:
                if mismatch > 1:
                    break
                elif j+1!=n and address[j+1]==name[k]:
                    j += 1
                    mismatch += 1
                elif k+1!=m and address[j]==name[k+1]:
                    k += 1
                    mismatch += 1
                elif k+1!=m and j+1!=n and\
                    address[j+1]==name[k+1]:
                    j += 1
                    k += 1
                    mismatch += 1
                else:
                    continue
            j += 1
            k += 1
        if j == n-1 or (j == n-2 and mismatch==0):
            d = calc_distance(object[i])
            if d < close:
                close = d
    return close

def calc_distance(x):
    if len(x) == 2:
        return sqrt(x[0]**2 + x[1]**2)
    if len(x) == 4:
        x1, y1 = x[0], x[1]
        x2, y2 = x[2], x[3]
        m = (y2-y1)/(x2-x1)
        xc = (y1 - m * x1) / 2.0 / m
        yc = - m * xc
        return sqrt(xc**2 + yc**2)
    
