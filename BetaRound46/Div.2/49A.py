import sys
input = sys.stdin.readline

s = input().strip().replace(' ','').replace('?','').lower()

if s[-1] in 'aeiouy':
    print('YES')
else:
    print('NO')