import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

if len(set(A)) >= k:
    ans = []
    visited = set()
    for i in range(n):
        if A[i] not in visited:
            ans.append(i+1) # 1-based
            visited.add(A[i])
            
        if len(ans) == k:
            break
    
    print('YES')
    print(*ans)
    
else:
    print('NO')