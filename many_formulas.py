N = 3
S = '125'
# 125
# 12 + 5
# 1 + 25
# 1 + 2 + 5

tot = 0
 
for bit in range(1<<(N-1)):
  tmp = 0
  print(bit)
  for i in range(N-1):
    tmp *= 10
    tmp += int(S[i])
    print(tmp)
 
    if bit & (1<<i):
      tot += tmp
      tmp = 0
  
  tmp *= 10
  tmp += int(S[N-1])
  print(tmp)
  tot += tmp
  print(tot)
  print("-"*10)
 
print(tot)