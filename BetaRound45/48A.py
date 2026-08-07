import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

if s1==s2==s3:
    print('?')
elif s1!=s2 and s2!=s3 and s3!=s1:
    print('?')
else:
    winner = -1
    lst = [s1, s2, s3]
    sorted_lst = sorted(lst)
    
    if sorted(['paper', 'rock', 'rock']) == sorted_lst:
        winner = lst.index('paper')
    elif sorted(['rock', 'scissors', 'scissors']) == sorted_lst:
        winner = lst.index('rock')
    elif sorted(['scissors', 'paper', 'paper']) == sorted_lst:
        winner = lst.index('scissors')
    else:
        print('?') # 두 명이 이기는 상황
        
    
    if winner==0:
        print('F')
    elif winner==1:
        print('M')
    elif winner==2: # else로 처리하면 두 명 이기는 상황에서도 출력 나옴
        print('S')