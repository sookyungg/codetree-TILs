n,m=map(int,input().split())
arr=[[0]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))

tax=0

def goldcount(r,c,k):
    gold=0
    for x in range(n):
        for y in range(n):
            if abs(r-x)+abs(c-y)<=k:
                gold+=arr[x][y]

    return gold

maxvalue=0
for x in range(n):
    for y in range(n):
        for k in range(n):
            tax=k*k+(k+1)*(k+1)
            if goldcount(x,y,k)*m >=tax and maxvalue < goldcount(x,y,k):
                maxvalue=goldcount(x,y,k)

print(maxvalue)