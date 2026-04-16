import sys, math
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

Max = max(A)
print(Max*n - sum(A))
