W = 15
w = [2, 1, 3, 2, 1, 5]
v = [3, 2, 6, 1, 3, 85]
N = len(w)

# 自分の実装
# def main():
#     dp = [[0] * (W+1) for _ in range(N)]
#     dp[0][w[0]] = v[0]

#     for i in range(N):
#         if i == 0:
#             for j in range(w[0], W):
#                 dp[0][j] = v[0]
#         for j in range(W+1):
#             if j >= w[i]:
#                 dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
#             else:
#                 dp[i][j] = dp[i-1][j]
    
#     return dp[N-1][W]

# print(main())

weight = [2, 1, 3, 2, 1, 5]

def main():
    for i in N:
        for w in W+1:
            if (w - weight[i] >= 0):



main()