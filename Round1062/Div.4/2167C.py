import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    has_odd = any(a%2==1 for a in A)
    has_even = any(a%2==0 for a in A)
    
    if has_odd and has_even:
        A.sort()
        
    print(*A)