def repeatedDNASequences(s):
    sset = set()
    result = set()
    for i in range(len(s) - 9):
        s10 = s[i:i+10]
        if s10 in sset:
            result.add(s10)
        else:
            sset.add(s10)
    result = list(result)
    result.sort()
    return result

