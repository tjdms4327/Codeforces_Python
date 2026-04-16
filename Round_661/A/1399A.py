import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    A.sort()
    
    if any(-A[i]+A[i+1] >= 2 for i in range(n-1)):
        print('NO')
    else:
        print('YES')
