import sys
input = sys.stdin.readline

n = int(input())

tot = n * (n+1) // 2

if tot%2==0:
    print(0)
else:
    print(1)
    
    