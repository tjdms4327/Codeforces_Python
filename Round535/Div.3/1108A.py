import sys, math
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    
    if l1<l2:
        a, b = l1, r2
    else:
        a, b = r1, l2
    
    print(a, b)