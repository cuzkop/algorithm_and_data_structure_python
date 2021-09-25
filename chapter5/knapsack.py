n = 6
weight = [2, 1, 3, 2, 1, 5]
value = [3, 2, 6, 1, 3, 85]
w = 15

dp = [[-1]*(w+1)]*(n+1)

def chmax(dp, i, w, b):
    # print(dp[i][w], b)
    if dp[i][w] < b:
        dp[i][w] = b

for i in range(n):
    for j in range(w):
        if j - weight[i] >= 0:
            # i = 5, j=9の場合
            # dp[6][9] vs dp[5][9-weight[5]] + value[5]

            # 1番目、重さ2のvalue vs 0番目。重さ0のvalue + value(3)
            chmax(dp, i+1, j, dp[i][j-weight[i]]+value[i])

        chmax(dp, i+1, j, dp[i][j])

print(dp)