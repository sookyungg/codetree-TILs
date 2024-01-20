n,m=map(int,input().split())
arr=list(map(int,input().split()))
num=list(map(int,input().split()))
d=dict()
for i in range(n):
    if arr[i] in d:
        d[arr[i]]+=1
    else:
        d[arr[i]]=1

for i in range(m):
    if num[i] in d:
        print(d[num[i]], end=' ')
    else:
        print(0, end=' ')