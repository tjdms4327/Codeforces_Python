import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    
    diff = a-b
    
    pos = diff * (k//2) + (a if k%2==1 else 0)
    
    print(pos)