n = 7
h = [2, 9, 4, 5, 1, 6, 10]
dp = [100]*n
dp[0] = 0

def chmin(dp, i, b):
    if dp[i] > b:
        dp[i] = b

for i in range(1, n):
    chmin(dp, i, dp[i-1] + abs(h[i]-h[i-1]))
    if i == 1:
        continue

    
    chmin(dp, i, dp[i-2] + abs(h[i]-h[i-2]))
        
print(dp)