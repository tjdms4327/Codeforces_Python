import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

H = Counter(A)
heights = [cnt for cnt in H.values()]
    
print(max(heights), len(heights))