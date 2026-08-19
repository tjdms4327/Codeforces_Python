import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
    
res = []
for a in A:
    if a%2:
        res.append(a)
    else:
        res.append(a-1)
            
print(*res)