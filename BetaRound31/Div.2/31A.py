import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if (A[i]==A[j]+A[k]) and (i!=j and j!=k and k!=i):
                print(i+1, j+1, k+1) # 1-based
                sys.exit()

print(-1)