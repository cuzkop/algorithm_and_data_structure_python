N = 999999999


def dfs(s): # 文字列 s で始まる七五三数の個数
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0 # s 自体が七五三数なら +1
    for c in '753':
        ret += dfs(s + c)
    return ret

print(dfs('0'))