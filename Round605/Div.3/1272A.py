import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    a, b, c = map(int, input().split())
    
    best = float('inf')
    for a0 in [a-1,a,a+1]:
        for b0 in [b-1, b, b+1]:
            for c0 in [c-1,c, c+1]:
                best = min(best, abs(a0-b0)+abs(b0-c0)+abs(c0-a0))
                
                
    print(best)