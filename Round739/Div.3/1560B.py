t=int(input())
for k in range(t):
    a,b,c = map(int, input().split())
    diff = abs(b - a)
    n = 2 * diff

    if max(a, b, c) > n:
        print(-1)
    else:
        c_opp = c + diff

        if c_opp > n:
            c_opp -= n

        print(c_opp)