import random
# W = random.randint(50, 200)
# a = [random.randint(1, 100) for _ in range(3)]

# print('W: ', W)
# print('a: ', a)

comb = []

def subset_sum(i: int, a: list[int], w: int) -> bool:
    if not a:
        if w == 0:
            return True
        else:
            return False
    if a[i] == w:
        return True
    return subset_sum(i+1, a[i+1:], w-a[i]) or subset_sum(i+1, a[i+1:], w)

ave_c = 1000
cnt_sum = 0
for i in range(ave_c):
    in_cnt = 0
    exists = False
    while not exists:
        W = random.randint(50, 500)
        A = [random.randint(10, 30) for _ in range(10)]
        # print('W: ', W)
        # print('A: ', A)
        exists = subset_sum(0, A, W)
        in_cnt += 1
        # print('cnt: ', in_cnt)
        # print(exists)
    cnt_sum += in_cnt

print(cnt_sum / ave_c)
# W, Aをrandintの設定値でランダムで選んだ時にTrueが出てくるまでの平均試行回数