import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()
n = len(s)
m = len(t)

i, j = n-1, m-1
common = 0
while i >= 0 and j >= 0 and s[i]==t[j]:
    i -= 1
    j -= 1
    common += 1
    
print(n+m - 2*common)