import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    if sum(A) % 2 == 1:
        print('NO')
    else:
        half = sum(A) // 2
        cnt = Counter(A)
        
        if half%2 == 1:
            if cnt[1]:
                print('YES')
            else:
                print('NO')     
        
