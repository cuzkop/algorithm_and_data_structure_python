# N個の正の整数a0,a1,...,aN－1が与えられます．これらに対して「N個の整数がすべて偶数ならば２で割った値に置き換える」という操作を，操作が行えなくなるまで繰り返します．何回の操作を行うことになるかを求めるアルゴリズムを設計してください．

n = 2
a = [8,16]
    # [4,2]
    # [2,1]

odd = True
cnt = 0
while True:
    for i in a:
        if i % 2 != 0:
            odd = False


    if odd == False:
        print(cnt)
        break

    a = list(map(int, map(lambda x: x/2, a)))

    cnt += 1

