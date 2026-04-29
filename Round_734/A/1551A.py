import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    k = n // 3
    c1 = c2 = k
    
    if n % 3 == 1:
        c1 += 1
    elif n % 3 == 2:
        c2 += 1
        
    print(c1, c2)
