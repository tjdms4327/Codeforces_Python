import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    if k in A:
        print('YES')
    else:
        print('NO')
