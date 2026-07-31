import sys
input = sys.stdin.readline

n, d = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(n):
        if (i!=j) and abs(A[i]-A[j])<=d:
            cnt += 1
            
print(cnt)