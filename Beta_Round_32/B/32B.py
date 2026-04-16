import sys
input = sys.stdin.readline

s = input().strip()

i = 0
result = ''
while i < len(s):
    if s[i:i+2] == '-.':
        result += '1'
        i += 2
    elif s[i:i+2] == '--':
        result += '2'
        i += 2
    elif s[i] == '.':
        result += '0'
        i += 1

print(result)
