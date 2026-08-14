import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if k == 0:
    if A[0] == 1:
        print(-1)
    else:
        print(1)
    sys.exit()
elif k == n:
    print(A[-1])
    sys.exit()

l, r = A[k-1], A[k]
if l == r:
    print(-1)
else:
    print(l)