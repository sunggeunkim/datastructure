'''
reference - https://codefights.com/interview-practice/task/dQD4TCunke2JQ98rj
Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.

Example

For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.

Input/Output

[time limit] 4000ms (py3)
[input] array.integer inputArray

An array of integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The maximum possible sum of a subarray within inputArray.
'''
def arrayMaxConsecutiveSum2(inputArray):
    max_sum = inputArray[0]
    max_sum_so_far = max_sum
    for i in range(1,len(inputArray)):
        if max_sum > 0:
            max_sum += inputArray[i]
        else:
            max_sum = inputArray[i]
        max_sum_so_far = max(max_sum, max_sum_so_far)
    return max_sum_so_far
    

