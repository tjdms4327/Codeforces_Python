import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

left = 0
for a in A:
    if a <= k:
        left += 1
    else:
        break

right = 0
for a in A[::-1]:
    if a <= k:
        right += 1
    else:
        break

tot = left + right
if tot > n:
    tot = n
    
print(tot)