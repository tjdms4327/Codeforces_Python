import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)

Maxes = [sorted_A[-2] if a == sorted_A[-1] else sorted_A[-1] for a in A]
Mins = [sorted_A[1] if a == sorted_A[0] else sorted_A[0] for a in A]

diff = [Maxes[i]-Mins[i] for i in range(n)]
print(min(diff))