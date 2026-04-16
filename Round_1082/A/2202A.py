import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    
    cand = x - 2*y
    if cand >= 0 and cand % 3 == 0 and x + 4*y >= 0:
        print("YES")
    else:
        print("NO")
