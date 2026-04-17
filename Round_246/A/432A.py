import sys
input = sys.stdin.readline

n, k = map(int, input().split())
Y = list(map(int, input().split()))

poss = [5-y for y in Y if 5-y>=k]
print(len(poss)//3)
