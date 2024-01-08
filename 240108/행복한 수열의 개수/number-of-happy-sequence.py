n,m=map(int,input().split())
arr=[[0]*n for _ in range(n)]

for i in range(n):
    arr[i]=list(map(int,input().split()))


cnt=0
for x in range(n):
    for y in range(n-m+1):
        if arr[x][y:y+m]==[arr[x][y]]*m:
            flag =1
    
    if flag==1:
        cnt+=1
        flag=0

for x in range(n):
    tmp=[]
    for y in range(n):
        tmp.append(arr[y][x])

    for k in range(n-m+1):
        if tmp[k:k+m] == [tmp[k]]*m:
            flag =1
    
    if flag==1:
        cnt+=1
        flag=0

    
    
print(cnt)