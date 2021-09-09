from util.measure_time import measure

# https://atcoder.jp/contests/abc051/tasks/abc051_b
# given K, N [int]
# 0 <= X, Y, Z <= K
# X + Y + Z = N
K = 2500
N = 7500

@measure
def main():
    # cnt = 0
    # for x in range(K):
    #     for y in range(K):
    #         z = N - (x + y)
    #         if 0 <= z <= K:
    #             cnt += 1
    cnt = [1 for x in range(K) for y in range(K) if N - K <= x + y <= N]
    return len(cnt)

print(main())