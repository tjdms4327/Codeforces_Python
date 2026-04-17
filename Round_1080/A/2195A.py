import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    if 67 in A:
        print('YES')
    else:
        print('NO')
