# Explosive Sum
# https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python
from time import time
start = time()

def g(k): return k*(3*k-1)//2

partitions = {}
partitions[0] = partitions [1] = 1
partitions[2] = 2

def exp_sum(n):
    if n < 3:
        return partitions[n]
    k = 1
    while g(k) <= n:
        if k % 2 == 1:
            partitions.setdefault(n, 0)
            partitions[n] += partitions.get(n-g(k), exp_sum(n-g(k)))
        else:
            partitions.setdefault(n, 0)
            partitions[n] -= partitions.get(n-g(k), exp_sum(n-g(k)))

        if n-g(k) not in partitions.keys():
            partitions.setdefault(n-g(k), 0)
            partitions[n-g(k)] = exp_sum(n-g(k))
        print(partitions)
        k += 1

    k = -1
    while g(k) <= n:
        if k % 2 == 1:
            partitions.setdefault(n, 0)
            partitions[n] += partitions.get(n-g(k), exp_sum(n-g(k)))
        else:
            partitions.setdefault(n, 0)
            partitions[n] -= partitions.get(n-g(k), exp_sum(n-g(k)))
        if n-g(k) not in partitions.keys():
            partitions.setdefault(n-g(k), 0)
            partitions[n-g(k)] = exp_sum(n-g(k))
        print(partitions)
        k -= 1
    return partitions[n]

print(exp_sum(5))
print(time()-start)
