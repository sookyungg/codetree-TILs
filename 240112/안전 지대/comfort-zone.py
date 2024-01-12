import sys
sys.setrecursionlimit(2500)

n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and arr[nx][ny]>k:
            visited[nx][ny]=1 
            dfs(nx,ny)

max_k=1
max_a=0

for k in range(1,100+1):
    cnt=0
    for i in range(n):
        for j in range(m):
            if 0<=i<n and 0<=j<m and visited[i][j]==0 and arr[i][j]>k:
                visited[i][j]=1
                cnt+=1
                dfs(i,j)
    
    if max_a <cnt:
        max_k=k
        max_a=cnt    
    
    visited=[[0]*m for _ in range(n)]

print(max_k,max_a)