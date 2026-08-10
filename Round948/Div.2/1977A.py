t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    if n == m:
        print('YES')
    elif n > m:
        if (n-m)%2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')