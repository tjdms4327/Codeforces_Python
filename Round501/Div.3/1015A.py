import sys
input = sys.stdin.readline

n, m = map(int, input().split())

points = [True]*(1+m)
points[0] = False

for _ in range(n):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        if points[x]:
            points[x] = False
            
cnt = sum(points)
print(cnt)

if cnt:
    print(*[idx for idx, x in enumerate(points) if x])