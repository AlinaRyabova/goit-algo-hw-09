import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    coin_used = [-1] * (amount + 1)
    
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

def measure_time(func, amount):
    start_time = time.time()
    result = func(amount)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    # Приклад для суми 113
    example_amount = 113
    print(f"Приклад для суми {example_amount}:")
    
    greedy_result = find_coins_greedy(example_amount)
    print("Жадібний алгоритм:", greedy_result)
    
    dp_result = find_min_coins(example_amount)
    print("Алгоритм динамічного програмування:", dp_result)
    
    # Приклад для іншого набору монет
    def find_coins_greedy_custom(amount, coins):
        result = {}
        for coin in coins:
            if amount >= coin:
                count = amount // coin
                amount -= coin * count
                result[coin] = count
        return result

    def find_min_coins_custom(amount, coins):
        dp = [float('inf')] * (amount + 1)
        coin_used = [-1] * (amount + 1)
        
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

        result = {}
        while amount > 0:
            coin = coin_used[amount]
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1
            amount -= coin

        return result

    custom_coins = [30, 24, 12, 6, 3, 1]
    example_amount_custom = 48
    print(f"\nПриклад для суми {example_amount_custom} з нестандартним набором монет {custom_coins}:")
    
    greedy_result_custom = find_coins_greedy_custom(example_amount_custom, custom_coins)
    print("Жадібний алгоритм:", greedy_result_custom)
    
    dp_result_custom = find_min_coins_custom(example_amount_custom, custom_coins)
    print("Алгоритм динамічного програмування:", dp_result_custom)
    
    print("\nПорівняння часу виконання для великих сум:")
    amounts = [1000, 10000, 50000, 100000]

    print("Жадібний алгоритм:")
    for amount in amounts:
        result, exec_time = measure_time(find_coins_greedy, amount)
        print(f"Сума: {amount}, Час виконання: {exec_time:.6f} сек")

    print("\nАлгоритм динамічного програмування:")
    for amount in amounts:
        result, exec_time = measure_time(find_min_coins, amount)
        print(f"Сума: {amount}, Час виконання: {exec_time:.6f} сек")
