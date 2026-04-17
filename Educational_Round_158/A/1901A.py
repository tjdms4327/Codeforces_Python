import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    
    diff = [A[i]-A[i-1] for i in range(1, n+1)]
    diff.append(2*(x - A[-1]))
    print(max(diff))
