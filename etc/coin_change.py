'''
Making changes: Given an input x, write a function to
determine the minimum number of coins required
 to make that exact amount of change
 
 reference: http://www.byte-by-byte.com/smallestchange/
'''
table = {}
def change(x, coins):
    if x == 0:
        return 0    # base case
    m = x // min(coins)     # minimum number of coins (if used the smallest coin)
    if not m * min(coins) == x:
        raise Exception('The coin system is not valid.')
    for coin in coins:
        if x - coin >= 0:
            if x-coin in table:
                c = table[x - coin]
            else:
                c = change(x - coin, coins)
                table[x - coin] = c
            if m > c + 1:
                m = c + 1
    return m

print(change(32, [25, 10, 5, 1]))
