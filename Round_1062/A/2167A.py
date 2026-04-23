import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    nums = set(map(int, input().split()))
    if len(nums)==1:
        print('YES')
    else:
        print('NO')
