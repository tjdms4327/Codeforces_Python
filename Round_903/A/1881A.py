import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()
    
    cur = x
    for i in range(8):
        if s in cur:
            print(i)
            break
        cur += cur
    else:
        print(-1)
