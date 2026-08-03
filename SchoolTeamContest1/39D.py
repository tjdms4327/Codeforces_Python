import sys
input = sys.stdin.readline

x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

if (x1==x2) or (y1==y2) or (z1==z2):
    print('YES')
else:
    print('NO')