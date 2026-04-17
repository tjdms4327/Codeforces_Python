import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
s = input().strip()

tot = [ s.count(str(i+1)) * A[i] for i in range(4) ]
print(sum(tot))
