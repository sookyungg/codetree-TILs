n,m=map(int,input().split())
arr=[[0]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

#최대 k 값 구하는 함수
def maxk(n):
    k=1
    while True:
        if n*n<=(k*k+(k+1)*(k+1)):
            break
        else:
            k+=1
    return k

K=maxk(n)

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
        for k in range(K):
            tax=k*k+(k+1)*(k+1)

            if goldcount(x,y,k)*m >=tax and maxvalue < goldcount(x,y,k):
                maxvalue=goldcount(x,y,k)

print(maxvalue)