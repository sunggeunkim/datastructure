def isRectangle(points):
    for i in range(len(points)):
        curr = points[i]
        if i == 0:
            prev, next = points[3], points[i+1]
        elif i == 3:
            prev, next = points[i-1], points[0]
        else:
            prev, next = points[i-1], points[i+1]
        if prev[0] == curr[0]:
            if curr[1] != next[1]: return False
        elif prev[1] == curr[1]:
            if curr[0] != next[0]: return False
        else:
            x1 = prev[0] - curr[0]
            y1 = prev[1] - curr[1]
            x2 = curr[0] - next[0]
            y2 = curr[1] - next[1]
            if y1*y2 != -x1*x2: return False
    return True
            
        

