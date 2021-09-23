n = 7
h = [2, 9, 4, 5, 1, 6, 10]
dp = [0]*n

for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[i]-h[i-1])
        continue

    dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]), dp[i-2] + abs(h[i]-h[i-2]))
        
print(dp)