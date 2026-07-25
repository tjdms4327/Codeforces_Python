import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    cnt = Counter(A)
    
    tot = (cnt[-1]%2)*2 + cnt[0]
    print(tot)
