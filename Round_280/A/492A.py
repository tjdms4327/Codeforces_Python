import sys
input = sys.stdin.readline

n = int(input())

total = 0
height = 0
for x in range(1, n+1):
    need = x * (x + 1) // 2
    if total + need > n:
        break
    total += need
    height += 1

print(height)
