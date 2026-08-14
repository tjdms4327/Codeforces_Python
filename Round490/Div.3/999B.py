import sys, math
input = sys.stdin.readline

n = int(input())
t = input().strip()

N = set()
for i in range(1, math.isqrt(n)+1):
    if n%i==0:
        N.add(i)
        N.add(n//i)

for i in sorted(list(N)):
    t = t[:i][::-1] + t[i:]
    
print(t)