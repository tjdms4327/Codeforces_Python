import sys
input = sys.stdin.readline

n, a, b, c = map(int, input().split())

cnt = 0
for double_half in range(a//2+1):
    temp = n - double_half
    for two in range(min(temp//2, c)+1):
        temp2 = temp - two*2

        if (not temp2) or (0<=temp2<=b):
            cnt += 1
            
print(cnt)