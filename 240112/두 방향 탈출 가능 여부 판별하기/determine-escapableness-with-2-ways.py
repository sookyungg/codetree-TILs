n,m=map(int,input().split())

arr=[[0]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]

for i in range(n):
    arr[i]=list(map(int,input().split()))

dx=[1,0]
dy=[0,1]

def dfs(x, y):

    visited[x][y] = 1
    
    for i in range(2):
        nx , ny = x + dx[i], y + dy[i]
        if (0 <= nx < n and 0 <= ny < m):
            if visited[nx][ny]==0 and arr[nx][ny]!=0:
                dfs(nx,ny)

dfs(0,0)
#print(visited)
print(visited[n-1][m-1])