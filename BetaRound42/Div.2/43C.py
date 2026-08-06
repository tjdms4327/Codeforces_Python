import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(input().strip().split())

remainer = [sum(map(int, a))%3 for a in A]
cnt = Counter(remainer)

tot = cnt[0]//2 + min(cnt[1], cnt[2])
print(tot)