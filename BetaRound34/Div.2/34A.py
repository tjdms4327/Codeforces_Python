import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

INF = float('inf')

ans = None
best = INF
for i in range(n):
    diff = abs(A[i%n] - A[(i+1)%n])
    if diff < best:
        best = diff
        ans = (i%n + 1, (i+1)%n + 1) # 1-based
        
print(*ans)