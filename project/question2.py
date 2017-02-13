def question2(a):
    if len(a) <= 1 or a == None:
        return a
    lmax = 1
    palmax = ""
    for i in range(1, len(a)-1):
        j = i - 1
        k = i + 1
        l = 1
        pal = a[i]
        while j >= 0 and k <= len(a)-1:
            if a[j] == a[k]:
                l += 2
                pal = a[j] + pal + a[k]
            j -= 1
            k += 1
        if l > lmax:
            palmax = pal
            lmax = l
    return palmax
