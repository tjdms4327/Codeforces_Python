import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    y = float('inf')
    for c in range(a, b+1):
        if (c-a)+(b-c) < y:
            y = (c-a) + (b-c)
    print(y)
