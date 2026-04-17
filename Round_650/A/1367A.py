import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    b = input().strip()
    a = [b[0]] + [b[i] for i in range(1, len(b), 2)]
    
    print(''.join(a))
