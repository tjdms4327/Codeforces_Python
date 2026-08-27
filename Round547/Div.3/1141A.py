import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if m%n != 0:
    print(-1)
    sys.exit()

cnt = 0
m //= n
while m%2==0:
    cnt += 1
    m //= 2
while m%3==0:
    cnt += 1
    m //= 3

if m==1:
    print(cnt)
else:
    print(-1)