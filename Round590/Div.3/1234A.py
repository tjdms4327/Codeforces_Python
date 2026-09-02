import sys, math
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n = int(input())
    A = list(map(int, input().split()))
    
    x = math.ceil(sum(A) / n)
    print(x)