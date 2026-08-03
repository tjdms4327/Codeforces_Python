import sys
input = sys.stdin.readline
 
s = input().strip()
t = input().strip()
 
if s == t[::-1]:
    print('YES')
else:
    print('NO')