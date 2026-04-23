t = int(input())
for _ in range(t):
    s = list(input().strip().split())
    res = ''.join(x[0] for x in s)
    print(res)
