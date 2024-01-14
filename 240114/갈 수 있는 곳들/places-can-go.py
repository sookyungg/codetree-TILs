from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start = [list(map(int, input().split())) for _ in range(k)]
visited = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0

def bfs(x, y):
    global cnt
    q = deque([(x, y)])
    
    if visited[x][y] == 0:
        cnt += 1
    
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

for x, y in start:
    x=x-1
    y=y-1
    bfs(x, y)
print(cnt)