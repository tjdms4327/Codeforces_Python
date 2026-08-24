import sys, math
input = sys.stdin.readline

n, x, y = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cnt = 0
if x > y:
    print(n)
else:
    cnt = sum(a<=x for a in A)
    print((cnt+1) // 2)