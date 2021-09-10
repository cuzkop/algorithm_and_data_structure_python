a = [2, 4, 8, 16]
# 32768 = 2^15

ans = 0

bit_v = a[0]

for i in a:
    print(bin(bit_v))
    bit_v = bit_v | i

# print(bin(bit_v))

for i in range(1000000):
    if bit_v & (1 << i):
        ans = i
        break

print(ans)
  
# 1     1
# 2    10
# 3    11
# 4   100
# 5   101
# 6   110
# 7   111
# 8  1000
# 9  1001
# 10 1010