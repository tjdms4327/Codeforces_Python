import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    line = input().strip().split()
    A = list(''.join(line).split('1'))
    
    print(max(len(a) for a in A))
