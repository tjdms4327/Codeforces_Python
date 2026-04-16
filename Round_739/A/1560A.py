import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    
    cur = 0
    while k > 0:
        cur += 1
        while cur%3==0 or cur%10==3:
            cur += 1
        k -= 1
    print(cur)
