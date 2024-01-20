from collections import deque
from copy import deepcopy

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
r1,c1=map(int, input().split())
r1,c1=r1-1,c1-1
r2,c2=map(int, input().split())
r2,c2=r2-1,c2-1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, clean_arr):
    visited=[[0]*n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and clean_arr[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
            if nx==r2 and ny==c2:
                visited[nx][ny]=visited[cx][cy]+1
                return visited[nx][ny]
                
    return visited[r2][c2]

# 벽의 수
walls=[]            
def wall_num(arr):
    global walls
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                walls.append([i,j])
    return 


#n개의 벽중에 k개 뽑는 함수
max_num=0
remove_list=[]
def choose(cur,cnt):
    global max_num
    clean_arr=deepcopy(arr)
    if cur==len(walls)+1:
        if cnt==k:
            #print(remove_list)
            for i in range(k):
                clean_arr[walls[remove_list[i]-1][0]][walls[remove_list[i]-1][1]]=0
            visited=bfs(r1,c1,clean_arr)
            #print(visited)
            max_num=max(max_num,visited)  
        return     
    remove_list.append(cur) 
    choose(cur+1,cnt+1)
    remove_list.pop()
    choose(cur+1,cnt)

wall_num(arr)
choose(1,0)
if max_num==0:
    print(-1)
else:
    print(max_num-1)