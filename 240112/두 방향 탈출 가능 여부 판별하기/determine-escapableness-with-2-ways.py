n,m=map(int,input().split())

arr=[[0]*n for _ in range(m)]
visited=[[0]*n for _ in range(m)]

for i in range(n):
    arr[i]=list(map(int,input().split()))

dx=[1,0]
dy=[0,1]

def dfs(x, y):

    visited[x][y] = 1

    for i in range(2):
        nx , ny = x + dx[i], y + dy[i]
        if can_go(nx,ny):
            dfs(nx,ny)


def can_go(x,y):
    if not(0 <= x and x < n and 0 <= y and y < m):
        return False
    
    if visited[x][y] or arr[x][y] == 0:
        return False
    
    return True
        
dfs(0,0)
#print(visited)
print(visited[n-1][m-1])