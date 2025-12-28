def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]

    # dp[i] stores the minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # last_coin[i] stores the last coin used to make amount i
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Reconstruct the solution by tracing back the used coins
    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

# Example usage
amount = 113

print("Greedy:", find_coins_greedy(amount))
print("DP:", find_min_coins(amount))

