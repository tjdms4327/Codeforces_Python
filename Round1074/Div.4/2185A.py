import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print(*range(1, n+1))