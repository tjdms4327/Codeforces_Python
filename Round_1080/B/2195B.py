import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = [0] + list(map(int, input().split()))
    
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            idx = []
            cur = i
            while cur <= n:
                idx.append(cur)
                visited[cur] = True
                cur *= 2
            
            values = sorted(A[j] for j in idx)
            for j, v in zip(sorted(idx), values):
                A[j] = v
    
    if A[1:] == sorted(A[1:]):
        print("YES")
    else:
        print("NO")
