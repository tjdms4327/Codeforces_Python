def Tanya_subtract(n):
    if (n%10!=0): return n-1
    else: return n//10

n, k=map(int, input().split())
result=n
for _ in range(k):
    result=Tanya_subtract(result)
print(result)