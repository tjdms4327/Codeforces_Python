import sys
input = sys.stdin.readline

month = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

s = input().strip()
k = int(input())

ans = (month.index(s)+k)%12
print(month[ans])