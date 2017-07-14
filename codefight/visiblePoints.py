import math

def visiblePoints(points):
    m = sorted([math.atan2(float(point[0]),float(point[1])) for point in points])
    max_points = 1
    j = 1
    for i in range(len(m)):
        while 0 <= m[j%len(m)] - m[i] <= math.pi/4 and j - i < len(m):
            j += 1
        if j - i > max_points:
            max_points = j - i
    return max_points
