from collections import deque

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        cx,cy=q.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and arr[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny]=visited[cx][cy]+1
    return visited

visited=bfs(0,0)
if visited[n-1][m-1]==0:
    print(-1)
else: 
    print(visited[n-1][m-1]-1)