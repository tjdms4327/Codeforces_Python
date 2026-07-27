import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    print(max(0, max(b,c)-a+1),
        max(0, max(a,c)-b+1),
        max(0, max(a,b)-c+1))