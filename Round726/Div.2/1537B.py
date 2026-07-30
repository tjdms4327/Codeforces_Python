import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

t = int(input())
for _ in range(t):
    n, m, i, j = map(int, input().split())
    
    cand = [(1,1), (1, m), (n,1), (n, m)]
    
    best = -1
    ans = None
    for x1, y1 in cand:
        for x2, y2 in cand:
            d = dist(i, j, x1, y1) + dist(x1, y1, x2, y2) + dist(i, j, x2, y2)
            if best <= d:
                ans = (x1, y1, x2, y2)
                best = d
                
    print(*ans)