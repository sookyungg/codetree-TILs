def find_next(x, y, direction):
    global n, grid
    next_list = []
    nx, ny = x + dx[direction], y + dy[direction]

    while 0 <= nx < n and 0 <= ny < n:
        if grid[x][y] < grid[nx][ny]:
            next_list.append((nx, ny))
        nx += dx[direction]
        ny += dy[direction]

    return next_list

def find_max_times(count, x, y):
    global max_times
    next_list = find_next(x, y, directions[x][y])

    if not next_list:
        max_times = max(max_times, count)

    for next_x, next_y in next_list:
        find_max_times(count + 1, next_x, next_y)

if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    directions = [list(map(int, input().split())) for _ in range(n)]
    start = list(map(int, input().split()))
    start[0] -= 1
    start[1] -= 1

    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    max_times = 0

    find_max_times(0, start[0], start[1])

    print(max_times)