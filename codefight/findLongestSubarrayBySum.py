def findLongestSubarrayBySum(s, arr):
    j, max_length, subsum = 0, 0, 0
    result = [-1]
    for i in range(len(arr)):    
        subsum += arr[i]
        while j < i and subsum > s:            
            subsum -= arr[j]
            j += 1
        if subsum == s:
            if i - j + 1 > max_length:
                max_length = i - j + 1
                result = [j+1, i+1]        
    return result
