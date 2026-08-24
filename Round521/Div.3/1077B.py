import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

light_off = 0
for i in range(1, n-1):
    if (A[i-1] == A[i+1] == 1) and A[i]==0:
        light_off += 1
        A[i+1] = 0
        
        
print(light_off)