def stringPermutations_helper(s, l, r, result):
    if l == r:
        result.add(''.join(s))
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]
            stringPermutations_helper(s, l+1, r, result)
            s[l], s[i] = s[i], s[l]
            
# recursive method      
def stringPermutations(s):
    result = set()
    stringPermutations_helper(list(s), 0, len(s)-1, result)
    return sorted(list(result))

