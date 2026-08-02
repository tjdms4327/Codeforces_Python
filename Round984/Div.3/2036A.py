import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    for i in range(n-1):
        temp = abs(A[i]-A[i+1])
        if temp not in [5, 7]:
            print('NO')
            break
    else:
        print('YES')