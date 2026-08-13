import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    
    diff = n - m
    if diff < r:
        r -= diff
    else:
        l += (diff - r)
        r = 0
        
    print(l, r)