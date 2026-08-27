import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
for _ in range(n):
    s = list(input().strip())
    s.sort()
    
    counter = Counter(s)
    if any(cnt>1 for cnt in counter.values()):
        print('No')
        continue
    
    lst = [ord(x) for x in s]
    
    if lst[-1]-lst[0] == len(s)-1:
        print('Yes')
    else:
        print('No')