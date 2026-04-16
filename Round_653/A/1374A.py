import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    
    k = x * ((n - y) // x) + y
    print(k)
