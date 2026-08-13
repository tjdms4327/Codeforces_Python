import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    
    x_move = math.ceil(x/k)
    y_move = math.ceil(y/k)
    
    if x_move <= y_move:
        print(2*y_move)
    else:
        print((x_move-1)*2 + 1)