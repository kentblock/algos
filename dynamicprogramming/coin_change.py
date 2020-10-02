# Basic recurise solution
# BUG in dynmaic programming solution
def coin_change(n, coins, largest_coin):
    """
    return number of ways to make change of n,
    with an infinite supply of coins of values given in coins
    """
    if n == 0:
        return 1
    if n < 0:
        return 0

    sum = 0
    for c in coins:
        if c >= largest_coin:
            sum += coin_change(n - c, coins, c)
    return sum

def coin_change_dp(n, coins, largest_coin, d):
    """
    better solution to the problem using dynamic programming
    DOESNT WORK
    """
    if n == 0:
        return 1

    if n < 0:
        return 0

    if d[n] != -1:
        print("saving time")
        return d[n]

    sum = 0
    for c in coins:
        if c >= largest_coin:
            sum += coin_change_dp(n - c, coins, c, d)
    d[n] = sum
    return sum


if __name__ == "__main__":
    """
    TESTING
    """
    coins = {1, 2, 3}
    n = 4
    d = [-1 for _ in range(n + 1)]
    print(coin_change(n, coins, 0))
    coin_change_dp(n, coins, 0, d)
    print(d[n])
    print(d)
    coins = {2, 5, 3, 6}
    n = 10
    d = [-1 for _ in range(n + 1)]
    print(coin_change(n, coins, 0))
    coin_change_dp(n, coins, 0, d)
    print(d)
    print(d[n])