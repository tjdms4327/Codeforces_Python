import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    k = n%10
    count = sum(1+2+3+4 for i in range(1, k))
    
    length = len(str(n))
    for i in range(1, length+1):
        count += i
        
    print(count)
