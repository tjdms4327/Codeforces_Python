import sys
input = sys.stdin.readline

def divisor_cnt(num):
    cnt = 0
    for i in range(2, num+1):
        if num%i == 0:
            cnt += 1
            while num%i==0:
                num //= i 
        if num==1:
            break
        
    return cnt
    

n = int(input())

almost_prime = [False]*(n+1)
for num in range(2, n+1):
    if divisor_cnt(num) == 2:
        almost_prime[num] = True

print(sum(almost_prime))