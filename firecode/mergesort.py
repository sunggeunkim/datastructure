def merge(a, b):
    merged_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
    if j < len(b) and i == len(a):
        merged_list += b[j:]
    if i < len(a) and j == len(b):
        merged_list += a[i:]
    return merged_list
        
def merge_sort_helper(a_list, i, j):
    if i == j:
        return [a_list[i]]
    elif i < j:
        m = (i + j) // 2
        low_a = merge_sort_helper(a_list, i, m)
        high_a = merge_sort_helper(a_list, m+1, j)
        return merge(low_a, high_a)

def merge_sort(a_list):
    '''[1,3,9,2,3,4,6]'''
    if a_list == None or len(a_list) < 2:
        return a_list
    return merge_sort_helper(a_list, 0, len(a_list)-1)

print(merge_sort([1,3,9,2,3,4,6]))
