import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    
    print(b[0]+a[1:], a[0]+b[1:])
