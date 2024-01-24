n=int(input())
MOD = 1000000007

dp=[0]*(n+1)

def stair(n):
    dp[0]=1
    dp[1]=1

    for i in range(1,n+1):
        if i>=2:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
        if i>=3:
            dp[i] = (dp[i] + dp[i - 3]) % MOD

stair(n)
print(dp[n-1])