# DP
# 1. for 문
# 2. 메모이제이션
# 3. Tabulation
n=int(input())
dp=[0,1]

def fibo(n):
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])

fibo(n)
print(dp[n])