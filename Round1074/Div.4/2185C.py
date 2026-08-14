import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted(list(map(int, input().split())))
    
    
    count = 0
    cur = 1
    for i in range(1, n):
        if A[i-1]+1 == A[i]:
            cur += 1
        elif A[i-1]!= A[i]:
            count = max(count, cur)
            cur = 1
    count = max(count, cur)
    
    print(count)
        