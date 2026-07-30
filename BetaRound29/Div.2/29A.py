import sys
input = sys.stdin.readline

n = int(input())
xd = [tuple(map(int, input().split())) for _ in range(n)]

for x1, d1 in xd:
    for x2, d2 in xd:
        if x1+d1==x2 and x2+d2==x1:
            print('YES')
            sys.exit()

print('NO')