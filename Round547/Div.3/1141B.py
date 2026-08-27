import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A += A

max_rest = 0

rest = []
for idx, val in enumerate(A):
    if val == 0:
        rest.append(idx)
        
for i in range(1, len(rest)):
    max_rest = max(max_rest, rest[i] - rest[i-1]-1)
        
print(max_rest)