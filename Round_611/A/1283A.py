import sys
input = sys.stdin.readline

time = 24 * 60

t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    left = time - (60*h+m)
    print(left)
