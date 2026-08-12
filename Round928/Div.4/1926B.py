import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [input().strip() for _ in range(n)]
    
    cnts = []
    for row in matrix:
        if '1' in row:
            cnts.append(row.count('1'))
            
    if len(set(cnts))==1:
        print('SQUARE')
    else:
        print('TRIANGLE')