import sys
input = sys.stdin.readline
from collections import Counter

s1 = input().strip()
s2 = input().strip()

cnt_s1 = Counter(s1)
cnt_s2 = Counter(s2)

for key, cnt in cnt_s2.items():
    if key==' ':
        continue
    
    if key in cnt_s1 and cnt_s1[key]>=cnt:
        continue
    else:
        print('NO')
        break
else:
    print('YES')