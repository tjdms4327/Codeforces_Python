import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    
    if k%2:
        print('YES')
    else:
        print('NO')