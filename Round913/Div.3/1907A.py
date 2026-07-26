import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, c = input().strip()
    
    for x in '12345678':
        if x == c:
            continue
        print(r+x)
    for y in 'abcdefgh':
        if y == r:
            continue
        print(y+c)