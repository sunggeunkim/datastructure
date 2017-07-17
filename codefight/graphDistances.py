'''
reference: https://codefights.com/interview-practice/task/QTirmApTj7sWaidLk/description
You have a connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

Given g and the index of a start vertex s, find the distances between the start vertex s and each of the vertices of the graph.

Example

For

g = [[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]]
and s = 0, the output should be
graphDistances(g, s) = [0, 2, 2].

Example

The distance from the start vertex 0 to itself is 0.
The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
The distance from the start vertex 0 to vertex 2 is 2.
Input/Output

[time limit] 4000ms (py3)
[input] array.array.integer g

The graph is represented as a square matrix, as described above.

Guaranteed constraints:
1 ≤ g.length ≤ 100,
g.length = g[i].length,
-1 ≤ g[i][j] ≤ 30.

[input] integer s

The start vertex (0-based).

Guaranteed constraints:
0 ≤ s < g.length.

[output] array.integer

An array, the ith element of which is equal to the distance between the start vertex s and the ith vertex of the graph g.
'''

def graphDistances(g, s):
    ans = [None for _ in range(len(g))] 
    ans[s] = 0
    q = [(s,0,set([s]))]
    while len(q):
        curr_index, dist, visited = q.pop()
        for dest_index in [x for x in range(len(g)) if g[curr_index][x] != -1 and x not in visited]:
            total_dist = dist + g[curr_index][dest_index]
            if ans[dest_index] == None or total_dist < ans[dest_index]:
                temp = visited.copy()
                temp.add(dest_index)
                ans[dest_index] = total_dist
                q.append((dest_index,total_dist,temp))
    return ans
    
