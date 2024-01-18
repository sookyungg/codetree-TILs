from collections import deque

n=int(input())
r1,c1,r2,c2=map(int,input().split())
r1,c1,r2,c2=r1-1,c1-1,r2-1,c2-1
arr=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]

move=[[-2,1],[-2,-1],[2,1],[2,-1],[-1,2],[-1,-2],[1,2],[1,-2]]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1

    while q:
        cx,cy=q.popleft()
        for m in move:
            nx=cx+m[0]
            ny=cy+m[1]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=visited[cx][cy]+1
            if nx==r2 and ny==c2:
                return visited

visited=bfs(r1,c1)
if visited==None:
    print(-1)
else:
    print(visited[r2][c2]-1)