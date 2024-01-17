from collections import deque

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start = [list(map(int, input().split())) for _ in range(k)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid, x, y):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return visited

def cnt_visit(grid):
    visit = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                visit += 1
    return visit

def clean_rocks(selected_rocks, rocks, rocks_cnt):
    clean_arr = [row[:] for row in arr]  # Make a copy of the original array
    for idx in selected_rocks:
        clean_arr[rocks[idx - 1][0]][rocks[idx - 1][1]] = 0

    total_visit = 0
    for e in start:
        r, c = e[0] - 1, e[1] - 1
        total_visit =cnt_visit(bfs(clean_arr, r, c))

    return total_visit

selected_rocks = []
rocks_cnt = 0
rocks = []
ans=0
def choose(cur, cnt, rocks_cnt):
    global total_visit
    global ans
    if cur == rocks_cnt + 1:
        if cnt == m:
            total_visit = clean_rocks(selected_rocks, rocks, rocks_cnt)
            ans=max(total_visit,ans)
            #print(ans)
        return ans
    selected_rocks.append(cur)
    choose(cur + 1, cnt + 1, rocks_cnt)
    selected_rocks.pop()
    choose(cur + 1, cnt, rocks_cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            rocks.append([i, j])
            rocks_cnt += 1

choose(1, 0, rocks_cnt)
print(ans)