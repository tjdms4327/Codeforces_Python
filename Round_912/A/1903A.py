import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    if len(set(A))==1 or A==sorted(A):
        print('YES')
    elif k == 1:
        print('NO')
    else:
        print('YES')
