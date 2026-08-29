import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]
    
    x_in, y_in = set(), set()
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == '#':
                x_in.add(r+1)
                y_in.add(c+1)
                
    x = (min(x_in) + max(x_in)) // 2
    y = (min(y_in) + max(y_in)) // 2
    
    print(x, y)