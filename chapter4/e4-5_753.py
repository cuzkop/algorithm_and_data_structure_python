from util.measure_time import measure

# https://atcoder.jp/contests/abc114/tasks/abc114_c
# ex: 735357
# given K
# 575 -> 4
# 3600 -> 13
# 999999999 -> 26484

K = 999999999

@measure
def main(k: int):
    sum = rec('3') + rec('5') + rec('7')
    return sum

def rec(num_str: str):
    if int(num_str) > K:
        return 0
    if int(num_str) <= K:
        if all(map(num_str.__contains__, ['7', '5', '3'])): # 3, 5, 7が全てnum_strに含まれているか
            return 1 + rec(num_str+'3') + rec(num_str+'5') + rec(num_str+'7')
        else:
            return rec(num_str+'3') + rec(num_str+'5') + rec(num_str+'7')

print(main(K))