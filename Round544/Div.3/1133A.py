import sys
input = sys.stdin.readline

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

tot_m = m1 + m2 + 60*(h1+h2)
ans = tot_m//2

print(f'{ans//60:02d}:{ans%60:02d}')