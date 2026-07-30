import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(1, max(A)+2):
    if i not in A:
        print(i)
        break