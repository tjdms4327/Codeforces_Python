import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = list(map(int, input().strip()))
    
    print(sum(n))
