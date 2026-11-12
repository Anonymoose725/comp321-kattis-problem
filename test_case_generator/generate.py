import random

N = random.randint(1, 10**5)
print(N)
for _ in range(N):
    a = random.randint(0, 10**5)
    b = random.randint(1, 10**5)
    c = random.randint(1, 10**5)
    print(a, b, c) # implicit \n