def tribonacci(n: int, memo: dict) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = tribonacci(n-1, memo) + tribonacci(n-2, memo) + tribonacci(n-3, memo)
    return memo[n]

# 0, 0, 1, 1, 2, 
# 4, 7, 13, 24, ...

n = 8
memo = {}
print(tribonacci(n, memo))