import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n = int(input())
    
    cnt = [0, 0, 0]
    while n%2 == 0:
        n //= 2
        cnt[0] += 1
    while n%3 == 0:
        n //= 3
        cnt[1] += 1
    while n%5 == 0:
        n //= 5
        cnt[2] += 1
        
    if n > 1:
        print(-1)
    else:
        x, y, z = cnt
        ans = z
        x += 2*z
        ans += y
        x += y
        ans += x
        print(ans)