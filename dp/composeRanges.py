'''
reference: https://codefights.com/interview-practice/task/cHYqbQ9DiWmejAdeG
Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].

Input/Output

[time limit] 4000ms (py3)
[input] array.integer nums

A sorted array of unique integers.

Guaranteed constraints:
0 ≤ nums.length ≤ 15,
-(231 - 1) ≤ nums[i] ≤ 231 - 1.

[output] array.string
'''

def composeRanges(nums):
    if nums == []:
        return []
    result = []
    start = nums[0]
    end = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start)+"->"+str(end))
            start = nums[i]
        end = nums[i]
    if start == end:
        result.append(str(start))
    else:
        result.append(str(start)+"->"+str(end))
    return result
