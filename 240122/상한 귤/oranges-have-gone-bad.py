from collections import deque

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[-2]*n for _ in range(n)]
oranges=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    for i,j in oranges:
        q.append((i,j))
        visited[i][j]=0

    while q:
        cx,cy=q.popleft()

        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-2 and arr[nx][ny]==1:
                visited[nx][ny]=visited[cx][cy]+1
                q.append((nx,ny))
    return visited

            
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            oranges.append((i,j))
        if arr[i][j]==0:
            visited[i][j]=-1
            
visited=bfs()

for i in range(n):
    for j in range(n):
        print(visited[i][j],end=' ')
    print()