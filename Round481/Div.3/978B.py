import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

ans = 0
cnt = 0

for c in s:
    if c == 'x':
        cnt += 1
        if cnt >= 3:
            ans += 1
    else:
        cnt = 0

print(ans)
