import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())

cnt = 0
for i in range(0, n, 2):
    if s[i:i+2] in [['a','a'], ['b','b']]:
        s[i] = 'a'
        s[i+1] = 'b'
        cnt += 1
        
print(cnt)
print(''.join(s))