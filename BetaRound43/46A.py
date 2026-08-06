import sys
input = sys.stdin.readline

n = int(input())

ans = []

cur = 1
for i in range(1, n):
    cur = (cur+i-1)%n + 1
    ans.append(cur)
    
print(*ans)