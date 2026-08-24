import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    
    if 2*a <= b:
        tot = n*a
    else:
        tot = (n//2)*b + (a if n%2 else 0)
        
    print(tot)