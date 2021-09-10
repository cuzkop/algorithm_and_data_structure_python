import random
import time

start = time.time()
inf = 1000

int_list = [random.randint(1, 100) for _ in range(100)]
N = random.randint(1, 100)

exist = False
found_id = -1
min_value = inf
print('N='+str(N), int_list)
for i, j in enumerate(int_list):
    if j < min_value:
        min_value = j

print(min_value)
min()

elapsed_time = time.time() - start

print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
