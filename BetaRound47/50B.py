import sys
input = sys.stdin.readline
from collections import Counter

s = input().strip()
counter = Counter(s)

tot = 0
for key, cnt in counter.items():
    tot += cnt*cnt
        
print(tot)