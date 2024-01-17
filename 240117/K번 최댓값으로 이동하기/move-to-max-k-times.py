# from collections import deque

# n,k=map(int, input().split())
# arr=[list(map(int,input().split())) for _ in range(n)]
# r,c=map(int,input().split())
# r,c=r-1,c-1
# visited=[[0]*n for _ in range(n)]

# dx=[0,0,-1,1]
# dy=[-1,1,0,0]

# def bfs(x,y):
#     q=deque()
#     q.append((x,y))
#     visited[x][y]==1 
#     while q:
#         cx,cy=q.popleft()
#         for i in range(4):
#             nx=cx+dx[i]
#             ny=cy+dy[i]
#             if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and arr[x][y]>arr[nx][ny]:
#                 visited[nx][ny]=1
#                 q.append((nx,ny))

# def best(x,y):
#     result=-1
#     rx,ry=-1,-1
#     for i in range(n):
#         for i in range(n):
#             if visited[i][j]==0 or (i,j)==(x,y):
#                 continue
#             else:
#                 if arr[i][j]>result:
#                     result=arr[i][j]
#                     rx,ry=i,j
#     if (ry, rx)==(-1, -1):
#         return -1,-1
#     return rx,ry

# for _ in range(k):
#     for i in range(n):
#         for j in range(n):
#             visited[i][j]=0
#     bfs(r,c)
#     ans_x,ans_y=best(r,c)
#     if (ans_y, ans_x)==(-1, -1):
#         break
#     else:
#         r,c=ans_x,ans_y

# print(r+1,c+1)
from collections import deque
n, k=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
sy, sx=map(int, input().split())
sy, sx=sy-1, sx-1
dy, dx=[-1, 0, 0, 1], [0, -1, 1, 0]
visited = [[False for _ in range(n)] for _ in range(n)]
def bfs(cur_y, cur_x):
    q=deque()
    q.append((cur_y, cur_x))
    visited[cur_y][cur_x]=True
    standard=grid[cur_y][cur_x]
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and grid[ny][nx]<standard:
                visited[ny][nx]=True
                q.append((ny, nx))
def find_best(cur_y, cur_x):
    result=-1
    ry, rx=-1, -1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j)==(cur_y, cur_x):
                continue
            else:
                if grid[i][j]>result:
                    result=grid[i][j]
                    ry, rx=i, j
    if (ry, rx)==(-1, -1):
        return -1, -1
    return ry, rx
for _ in range(k):
    for i in range(n):
        for j in range(n):
            visited[i][j]=False
    bfs(sy, sx)
    ans_y, ans_x=find_best(sy, sx)
    if (ans_y, ans_x)==(-1, -1):
        break
    else:
        sy, sx=ans_y, ans_x
print(sy+1, sx+1)