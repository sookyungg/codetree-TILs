n,m=map(int,input().split())
arr=list(map(int,input().split()))
num=list(map(int,input().split()))

for i in range(m):
    print(arr.count(num[i]), end=' ')