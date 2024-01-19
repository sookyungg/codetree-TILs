from collections import deque
n,h,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    visited=[[0]*n for _ in range(n)]
    q=deque()
    q.append((x,y))
    visited[x][y]=1

    while q:
        cx,cy=q.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]

            if 0<=nx<n and 0<=ny<n and (arr[nx][ny]==0 or arr[nx][ny]==2) and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=visited[cx][cy]+1   

            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==3 and visited[nx][ny]==0:
                visited[nx][ny]=visited[cx][cy]+1 
                return visited[nx][ny]-1

people=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            people.append([i,j])

answer=[[0]*n for _ in range(n)]
for p in people:
    if bfs(p[0],p[1])==None:
        answer[p[0]][p[1]]=-1
    else:
        answer[p[0]][p[1]]=bfs(p[0],p[1])

for i in range(n):
    for j in range(n):
        print(answer[i][j],end=' ')
    print()