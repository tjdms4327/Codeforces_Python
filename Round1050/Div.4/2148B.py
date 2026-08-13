import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    A = list(map(float, input().split())) # y좌표
    B = list(map(float, input().split())) # x좌표
    
    print(n+m)