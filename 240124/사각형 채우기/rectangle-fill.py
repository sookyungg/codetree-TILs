n=int(input())

dp=[0]*(1001)

def square(n):   
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

square(n)
print(dp[n]%10007)