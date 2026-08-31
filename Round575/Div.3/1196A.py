import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    a, b, c = map(int, input().split())
    
    cand = a+b+c
    print(cand//2)
    