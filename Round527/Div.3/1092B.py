import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

solve = 0
for i in range(0, n, 2):
    diff = A[i+1] - A[i]
    solve += diff
    
print(solve)