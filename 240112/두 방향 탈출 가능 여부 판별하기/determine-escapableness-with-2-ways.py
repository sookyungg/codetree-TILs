# n,m=map(int,input().split())

# arr=[[0]*n for _ in range(m)]
# visited=[[0]*n for _ in range(m)]

# for i in range(n):
#     arr[i]=list(map(int,input().split()))

# dx=[1,0]
# dy=[0,1]

# def dfs(x, y):
#     visited[x][y] = 1

#     for i in range(2):
#         nx , ny = x + dx[i], y + dy[i]
#         if can_go(nx,ny):
#             dfs(nx,ny)


# def can_go(x,y):
#     if not(0 <= x and x < n and 0 <= y and y < m):
#         return False
    
#     if visited[x][y] or arr[x][y] == 0:
#         return False
    
#     return True
        
# dfs(0,0)
# #print(visited)
# print(visited[n-1][m-1])   
def dfs(x, y):

    visited[x][y] = True
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x , new_y = x + dx, y + dy
        if can_go(new_x,new_y):
            dfs(new_x,new_y)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

n , m = tuple(map(int,input().split()))
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [[False for _ in range(m)]for _ in range(n)]

dfs(0 ,0)

if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)