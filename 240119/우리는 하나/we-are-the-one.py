from collections import deque
from copy import deepcopy
n,k,u,d=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def cango(x,y):
    if 0<=x<n and 0<=y<n and visited[x][y]==0:
        return True
    else:
        return False

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
            if cango(nx,ny) and u<=abs(arr[cx][cy]-arr[nx][ny])<=d:
                q.append((nx,ny))
                visited[nx][ny]=1
    return visited 

print(bfs(1,0))

# 갈수 있는 도시 찾는 함수
idx_arr=[]
def best(cities):
    city_cnt=0
    tmp=[[0]*n for _ in range(n)]    
    for i in range(n):
        for j in range(n):
            idx_arr.append([i,j])
    
    for city in cities:
        x,y=idx_arr[city-1]
        visited=bfs(x,y)
        #print(visited)
        for i in range(n):
            for j in range(n):
                if visited[i][j]==1:
                    tmp[i][j]=1
    print(tmp)
    for i in range(n):
            for j in range(n):
                if tmp[i][j]==1:
                    city_cnt+=1
    return city_cnt

#도시 중에 k개 고르는 함수 
cities=[]
max_num=0
def choose(cur,cnt):
    global max_num
    if cur==n*n+1:
        if cnt==k:       
            print(cities)
            max_num=max(best(cities),max_num)
            #print(max_num)
        return 
    cities.append(cur)
    choose(cur+1,cnt+1)
    cities.pop()
    choose(cur+1,cnt)

#choose(1,0)
#print(max_num)