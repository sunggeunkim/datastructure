'''
Given a positive integer, print all possible sum combinations using positive integers
'''
def print_all_sum_rec(target_sum, current_sum, x, results):
    if current_sum == target_sum:
        print(results)
    for i in range(x, target_sum):
        temp_sum = i + current_sum
        if temp_sum <= target_sum:
            results.append(i)
            print_all_sum_rec(target_sum, temp_sum, i, results)
            del results[-1]
        else:
            return


# 4
# 1, 1, 1, 1
# 1, 2, 1
# 2, 2
#...
def print_all_sum(target):
    results = []
    print_all_sum_rec(target, 0, 1, results)

print_all_sum(4)
