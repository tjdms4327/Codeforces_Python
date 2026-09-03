import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    
    a  = n // k
    left = n - a * k
    
    if left <= k//2:
          print(n)
    else:
        tot = n - (left-k//2)
        print(tot)
    