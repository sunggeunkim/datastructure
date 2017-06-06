# /*
# 
# Given a start and end time of a shift and the profit, 
# figure out the most you can make from the given shifts without them overlapping:
# 
# input:
# (1,3) - 5
# (2,5) - 6
# (4,6) - 5 <<<<<<<< 10
# (6,8) - 11 <<<<<<<< 21
# (6,7) - 4 <<<<<<<< 14
# (7,9) - 20 <<<<<<< 34
# (7,10) - 2
#
# output:
# 17
# 
# 
# */
def is_overlap(x, y):
    return x[1] > y[0]

def get_max_profit(input_shifts, profit):
    if len(input_shifts) == 0:
        return 0
    max_profit = [profit[0]]
    for i in range(1, len(profit)):
        found = False
        m = 0
        for j in range(i-1, -1, -1):
            if not is_overlap(input_shifts[j], input_shifts[i]) and max_profit[j] > m:
                m = max_profit[j]
                found = True                
        if found:
            max_profit.append(profit[i] + m)
        else:
            max_profit.append(profit[i])
            
    return max(max_profit)

print(get_max_profit([(1,3)], [5]))
print(get_max_profit([(1,3), (2,5)], [5, 6]))
print(get_max_profit([(1,3), (2,5), (4,6) ], [5, 6, 5]))
print(get_max_profit([(1,3), (2,5), (4,6), (5,10),(6,9) ], [5, 6, 5, 10, 7]))
print(get_max_profit([(1,3), (2,5), (4,6), (5,10),(6,9) ], [5, 6, 5, 12, 7]))
