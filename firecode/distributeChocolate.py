def distributeChocolate(points):
    if points == None or len(points) == 0:
        return 0
    c = [1]*len(points)
    for i in range(1,len(points)):
        if points[i] > points[i-1]:
            c[i] = c[i-1] + 1
    for i in range(len(points)-2,0,-1):
        if points[i] > points[i+1]:
            c[i] = max(c[i], c[i+1]+1)
    return sum(c)

print(distributeChocolate([2, 3, 3, 2, 1, 5, 2]))
