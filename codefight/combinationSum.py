# Recursive call
def DFS(candidates,target,result,intermedia):
    if target == 0:
        tmp = "(" + " ".join(map(str, intermedia)) + ")"
        result.append(tmp)
    for x in candidates:
        if x > target:
            return
        if intermedia == [] or x >= intermedia[-1]:
            DFS(candidates,target-x,result,intermedia+[x])
            
# Recursive solution
def combinationSum(a, sum):
    a = sorted(set(a))
    result = []
    DFS(a, sum, result, [])
    if result == []:
        return "Empty"
    return "".join(result)
