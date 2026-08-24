import sys, math
input = sys.stdin.readline
from collections import Counter

n = int(input())
D = list(map(int, input().split()))

Max = max(D)
counter = Counter(D)

primes = set()
for i in range(1, math.isqrt(Max)+1):
    if Max%i== 0:
        primes.add(i)
        primes.add(Max//i)
    
left = set()
for d in D:
    if counter[d] >= 2:
        left.add(d)
    else:
        if d not in primes:
            left.add(d)
            
print(Max, max(left))