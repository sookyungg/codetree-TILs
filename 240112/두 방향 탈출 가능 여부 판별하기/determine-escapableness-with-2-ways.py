n,m=map(int,input().split())
arr=[[0]*n for _ in range(m)]
visited=[[0]*n for _ in range(m)]

for i in range(n):
    arr[i]=list(map(int,input().split()))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and visited[x][y]==1 and arr[x][y]==0:
            dfs(nx,ny)
        
dfs(0,0)
print(visited[n-1][m-1])