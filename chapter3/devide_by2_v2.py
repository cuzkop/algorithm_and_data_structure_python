# N個の正の整数a0,a1,...,aN－1が与えられます．これらに対して「N個の整数がすべて偶数ならば２で割った値に置き換える」という操作を，操作が行えなくなるまで繰り返します．何回の操作を行うことになるかを求めるアルゴリズムを設計してください．

a = [8,12,40]
    # [4,2]
    # [2,1]

def how_many_devide_by2(n):
    cnt = 0
    while n % 2 == 0:
        n /= 2
        cnt += 1
    
    return cnt

print(min(map(how_many_devide_by2, a)))