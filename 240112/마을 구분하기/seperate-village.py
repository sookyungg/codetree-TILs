n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

p=[]
p_cnt=0

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y):
    global p_cnt
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and arr[nx][ny]==1:
            visited[nx][ny]=1
            p_cnt+=1
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if 0<=i<n and 0<=j<n and visited[i][j]==0 and arr[i][j]==1:
            visited[i][j]=1
            p_cnt=1
            dfs(i,j)
            p.append(p_cnt)

p.sort()
print(len(p))
for i in p:
    print(i)