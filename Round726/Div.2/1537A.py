import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int, input().split()))
    
    need = n - sum(B)
    if need == 0:
        print(0)
    elif need > 0:
        print(1)
    else:
        print(-need)