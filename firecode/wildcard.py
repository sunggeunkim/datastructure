def match(first, second):
    i = 0
    j = 0
    while j < len(second):
        if i > len(first)-1:
            return False
        if first[i] == '?':
            i += 1
            j += 1
            continue
        if first[i] == '*':
            i += 1
            while first[i] == '*':
                i += 1
            if first[i] == '?':
                j += 1
                continue
            while first[i] != second[j]:
                j += 1
                if j > len(second)-1:
                    return False
            i += 1
            j += 1
            continue
        if first[i] != second[j]:
            return False
        i += 1
        j += 1
    return True

print(match('fi*d?', 'firecodee'))
