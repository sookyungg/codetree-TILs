n=int(input())
MOD = 10007

dp=[0]*(n+1)

def stair(n):
    dp[0] = 1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(1,n+1):
        dp[i] = (dp[i - 2] + dp[i - 3]) % MOD

stair(n)
print(dp[n])