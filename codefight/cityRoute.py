'''
There are n islands and these islands are connected via one-way roads.
Find the cost of the path from 0 to n-1th island which gives the lowest cost.
Example

For

city = [[-1, 5, 20],
        [21, -1, 10],
        [-1, 1, -1]]
the output should be nightRoute(city) = 15.

city[i][j] equals the distance between the ith and the jth islands in miles, 
or -1 if there is no bridge by which one can move from island i to island j.

'''
def nightRoute(city):
    return nightRouteFinder(0, len(city), city, set([0]))


def nightRouteFinder(i, n, city, visited):
    if i == n - 1:
        return 0
    cost = []
    for j in range(n):
        newvisited = set(visited)
        if j not in visited and i != j and city[i][j] != -1:
            newvisited.add(j)
            cost.append(city[i][j] + nightRouteFinder(j, n, city, newvisited))
    if len(cost) > 0:
        return min(cost)
    else:
        return 0

city = [[-1,-1,19,8,18,-1,-1,-1,-1,-1],
 [10,6,4,7,0,10,18,-1,0,-1],
 [-1,-1,15,-1,17,3,-1,14,16,3],
 [4,19,3,15,8,4,6,11,5,8],
 [5,3,10,-1,0,14,15,1,16,5],
 [-1,8,-1,-1,5,-1,5,0,1,-1],
 [-1,18,-1,19,2,-1,10,-1,8,6],
 [14,8,12,16,-1,-1,0,16,15,17],
 [4,5,1,12,0,4,8,15,1,-1],
 [13,7,17,-1,4,13,16,3,12,9]]

print(nightRoute(city))

city = [[-1,5,20],
 [21,-1,10],
 [-1,1,-1]]

print(nightRoute(city))
