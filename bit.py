n = 5
w = 10
a = [1, 2, 4, 5, 11]

# 2の5乗で全探索できる
for bit in range(1<<n):
    sum = 0
    # 0~31(5桁)の2進数の0桁目から4桁目が論理積=1になるかを検査し、1になったらその値を足す
    for i in range(n):
        if bit & (1 << i):
            sum += a[i]
    
    if sum == w:
        print(bin(bit))
