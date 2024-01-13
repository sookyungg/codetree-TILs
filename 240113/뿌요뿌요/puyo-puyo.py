import sys
sys.setrecursionlimit(100000)

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
cnt=0

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(x,y):
    global cnt
    visited[x][y]=1
    cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
            if arr[x][y]==arr[nx][ny]:
                dfs(nx,ny)

    if cnt>=4:
        return 1
    else: 
        return 0

ans_cnt=0
ans_area=0

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt=0
            if dfs(i,j)==1:
                #print(cnt)
                ans_cnt=max(ans_cnt,cnt)
                ans_area+=1
            else:
                ans_cnt=max(ans_cnt,cnt)
            
print(ans_area, ans_cnt)