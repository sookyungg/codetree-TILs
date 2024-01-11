n,m=map(int,input().split())

arr=[[0]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]

for i in range(n):
    arr[i]=list(map(int,input().split()))

dx=[1,0]
dy=[0,1]

def dfs(x, y):

    visited[x][y] = 1
    
    for i in range(2):
        new_x , new_y = x + dx[i], y + dy[i]
        if can_go(new_x,new_y):
            dfs(new_x,new_y)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or arr[x][y] == 0:
        return False
    
    return True
        
dfs(0,0)
#print(visited)
print(visited[n-1][m-1])