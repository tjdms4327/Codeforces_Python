import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    
    if A[0]+k < A[-1]-k:
        print(-1)
    else:
        print(A[0]+k)