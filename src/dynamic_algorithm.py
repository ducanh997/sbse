def knapsack(weight_limit, weights, values):
    n = len(values)
    dp = [[0 for _ in range(weight_limit + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, weight_limit + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    max_value = dp[n][weight_limit]

    items = []
    temp_max_value = max_value
    temp_weight = weight_limit
    for i in range(n, 0, -1):
        if temp_max_value <= 0:
            break
        if temp_max_value == dp[i - 1][temp_weight]:
            continue
        else:
            items.append(i - 1)
            temp_max_value = temp_max_value - values[i - 1]
            temp_weight = temp_weight - weights[i - 1]

    return max_value, items


if __name__ == '__main__':
    values = [60, 100, 120, 120]
    weights = [10, 20, 30, 20]
    weight_limit = 50

    max_value, items = knapsack(weight_limit, weights, values)

    print(f'Max value: {max_value}')
    print(f'Items {items}')
