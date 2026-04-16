import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()

    half = len(s) // 2
    if s[:half]*2 == s:
        print('YES')
    else:
        print('NO')
