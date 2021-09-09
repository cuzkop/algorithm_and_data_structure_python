from util.measure_time import measure

# https://atcoder.jp/contests/abc045/tasks/arc061_a


S = '9999999999'
N = len(S)

# 3+2+4+5+3
# 最大の+の数はN-1

@measure
def main():
    ans = 0
    for bit in range(2**(N-1)):
        ope_locs = _ope_locs(bit=bit, n=N)
        splited_nums = _splitted_nums(num_str=S, ope_locs=ope_locs)
        ans += sum(splited_nums)
    return ans

def _ope_locs(bit: int, n: int) -> list[int]:
    ope_loc = []
    for i in range(n):
        if bit & (1 << i):
            ope_loc.append(i)
    return ope_loc

def _splitted_nums(num_str: str, ope_locs: list[int]) -> list[int]:
    previous_i = 0
    splitted_nums = []
    for i in ope_locs:
        splitted_nums.append(int(num_str[previous_i:i+1])) #iは文字列の最初の文字より1個だけ進んだ位置からカウントが始まっている
        previous_i = i+1
    splitted_nums.append(int(num_str[previous_i:]))
    return splitted_nums

print(main())