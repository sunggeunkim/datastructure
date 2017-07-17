'''
reference: https://codefights.com/interview-practice/task/idSmSy6u2LNiNDjKw/description
In San Francisco, there is a row of several beautiful houses called the Painted Ladies. Each of the Painted Ladies can be painted with one of three colors: red, blue or green. The cost of painting each house with a certain color is different. cost[i][0] for each i is the cost of painting house i red, cost[i][1] is the cost of painting it blue, and cost[i][2] is the cost of painting it green.

You want to paint all the houses in a way such that no two adjacent Painted Ladies have the same color. Find the minimum cost to achieve this.

Example

For cost = [[1, 3, 4], [2, 3, 3], [3, 1, 4]], the output should be
paintHouses(cost) = 5.

You can paint the first Painted Lady red for a cost of 1, the second one green for a cost of 3, and the third one blue for a cost of 1, for a total cost of 5.

Input/Output

[time limit] 4000ms (py3)
[input] array.array.integer cost

The costs of painting each Painted Lady a certain color following the guidelines: cost[i][0] for each i is the cost of painting house i red, cost[i][1] is the cost of painting it blue, and cost[i][2] is the cost of painting it green.

Guaranteed constraints:
1 ≤ cost.length ≤ 105,
cost[i].length = 3,
1 ≤ cost[i][j] ≤ 104.

[output] integer

The minimal cost of painting all the Painted Ladies so that no two adjacent houses are the same color.
'''

def paintHouses(cost):
    dp = [0, 0, 0]
    for house in cost:
        dp[0], dp[1], dp[2] = min(dp[1], dp[2]) + house[0]\
                             ,min(dp[0], dp[2]) + house[1]\
                             ,min(dp[0], dp[1]) + house[2]
    return min(dp)
        
