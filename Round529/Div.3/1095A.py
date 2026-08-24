import sys
input = sys.stdin.readline

n = int(input())
t = list(input().strip())

s = ''
i = 0
cnt = 1
while i < n:
    s += t[i] 
    cnt += 1
    i += cnt
    
print(s)