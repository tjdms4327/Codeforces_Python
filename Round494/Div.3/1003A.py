import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
mode = counter.most_common(1)[0][1]

print(mode)