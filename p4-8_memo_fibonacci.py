from util.measure_time import measure

@measure
def fibonacci(n: int, memo: dict[str, int]) -> int:
    if n == 1 or n==2:
        return 1
    # if n-1 in memo:
    #     n_1 = memo[n-1]
    # else:
    #     n_1 = fibonacci(n-1, memo)
    #     memo[n-1] = n_1
    # if n-2 in memo:
    #     n_2 = memo[n-2]
    # else:
    #     n_2 = fibonacci(n-2, memo)
    #     memo[n-2] = n_2
    # return n_1 + n_2 -- 最初の実装
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = int(input())
memo = {}

# 1, 1, 2, 3, 5, 8, 11

print(fibonacci(n, memo))