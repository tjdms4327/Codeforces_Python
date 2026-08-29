import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    G = [list(map(int, input().split())) for _ in range(n)]
    
    P = [-1]*(2*n)
    for i in range(n):
        j1 = 0
        j2 = n-1
        P[i+j1+1] = G[i][j1]
        P[i+j2+1] = G[i][j2]
    
    used = set(P)
    for x in range(1, 2*n+1):
        if x not in P:
            P[0] = x
            break
        
    print(*P)