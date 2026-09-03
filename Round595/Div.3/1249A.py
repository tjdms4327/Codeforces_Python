import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    ans = 1
    for i in range(1, n):
        if A[i]-A[i-1] == 1:
            ans = 2
            break
        
    print(ans)