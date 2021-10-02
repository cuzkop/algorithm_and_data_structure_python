n = 6
weight = [2, 1, 3, 2, 1, 5]
value = [3, 2, 6, 1, 3, 85]
w = 15

dp = [[0]*(w+1) for _ in range(n+1)]

def chmax(dp, i, w, b):
    if dp[i][w] < b:
        dp[i][w] = b

for i in range(n):
    for j in range(w+1):
        if j - weight[i] >= 0:
            chmax(dp, i+1, j, dp[i][j-weight[i]]+value[i])

        chmax(dp, i+1, j, dp[i][j])

print(dp)