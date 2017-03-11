class PairNum:
    def __init__ (self, number, i, j):
        self.number = number
        self.ind1 = i
        self.ind2 = j
        
def getKey(item):
    return item.number
    
def isUniquePairs(pairA, pairB):
    return ((pairA.ind1 != pairB.ind1) and (pairA.ind1 != pairB.ind2)\
        and (pairA.ind2 != pairB.ind1) and (pairA.ind2 != pairB.ind2))
    
def quadruple_sum(integer_list, target_number):
    if integer_list == None or target_number == None:
        return None
    if len(integer_list) < 4:
        raise ValueError('Not enough numbers are provided in integer_list.')
        
    output = []
    pair_sum = []
    import pdb;pdb.set_trace()
    for i in range(len(integer_list)):
        for j in range(i+1,len(integer_list)):
            pair_sum.append(PairNum(integer_list[i] + integer_list[j], i, j))

    pair_sum.sort(key=getKey)
    print([(pair_sum[i].ind1, pair_sum[i].ind2) for i in range(len(pair_sum))]) 
    print([(integer_list[pair_sum[i].ind1], integer_list[pair_sum[i].ind2]) for i in range(len(pair_sum))]) 
    print([pair_sum[i].number for i  in range(len(pair_sum))])
    i = 0
    j = len(pair_sum)-1
    while i < len(pair_sum) and j >= 0:
        #print(i,j)
        print((integer_list[pair_sum[i].ind1], integer_list[pair_sum[i].ind2],
                               integer_list[pair_sum[j].ind1], integer_list[pair_sum[j].ind2]))
        print((pair_sum[i].ind1, pair_sum[i].ind2,
                               pair_sum[j].ind1, pair_sum[j].ind2))
        print(pair_sum[i].number,pair_sum[j].number)
        print(isUniquePairs(pair_sum[i], pair_sum[j]))
        if pair_sum[i].number + pair_sum[j].number == target_number:
            if isUniquePairs(pair_sum[i], pair_sum[j]):
                output.append(tuple(sorted((integer_list[pair_sum[i].ind1], integer_list[pair_sum[i].ind2],
                               integer_list[pair_sum[j].ind1], integer_list[pair_sum[j].ind2]))))
            i += 1
            j -= 1
        elif pair_sum[i].number + pair_sum[j].number > target_number:
            j -= 1
        else:
            i += 1
    return list(set(output))
    
    
print(quadruple_sum([-2,-1,0,0,1,2],0))
