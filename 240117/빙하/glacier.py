from collections import deque
from copy import deepcopy

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
#print(n,m)
q=deque()

dx=[0,0,1,-1]
dy=[-1,1,0,0]

def cango(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        cx,cy=q.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if cango(nx,ny):
                if arr[nx][ny]==1:
                    tmp[nx][ny]=0
                if arr[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))

cnt=0
ices=[]
while True:
    visited=[[0]*m for _ in range(n)]
    cnt+=1
    ice=0
    for i in range(n):
        ice+=sum(arr[i])
    if ice==0:
        break
    else:
        ices.append((cnt,ice))
    tmp=deepcopy(arr)
    bfs(0,0)
    arr=deepcopy(tmp)

print(*ices[-1])