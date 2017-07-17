'''
reference - https://codefights.com/interview-practice/task/4MoqQLaw22nrzXbgs

You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.

Example

For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
sumInRange(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.

Input/Output

[time limit] 4000ms (py3)
[input] array.integer nums

An array of integers.

Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-1000 ≤ nums[i] ≤ 1000.

[input] array.array.integer queries

An array containing sets of integers that represent the indices to query in the nums array.

Guaranteed constraints:
1 ≤ queries.length ≤ 3 · 105,
queries[i].length = 2,
0 ≤ queries[i][j] ≤ nums.length - 1,
queries[i][0] ≤ queries[i][1].

[output] integer

An integer that is the sum of all of the sums gotten from querying nums, taken modulo 109 + 7.
'''

def sumInRange(nums, queries):
    if not queries or not nums:
        return 0
    prefixsum = []
    psum = 0
    for n in nums:
        psum += n
        prefixsum.append(psum)        
    s = 0
    for query in queries:
        s += prefixsum[query[1]]
        if query[0] > 0:
             s -= prefixsum[query[0]-1]
    return s % (10**9 + 7)

