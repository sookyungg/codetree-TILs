from collections import deque


def isRange(r, c):
    if 1 <= r <= m and 1 <= c <= n:
        return True
    return False


n, m, k = map(int, input().split())
board = [[0] * (m + 1) for _ in range(n + 1)]
history = []

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         history.append((i,j))


for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))


def selectAttacker(board):
    min_blood = 5001
    attacker_r = 0
    attacker_c = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != 0:
                # 공격력이 가장 낮은 포탑 선정
                if board[i][j] < min_blood:
                    min_blood = board[i][j]
                    attacker_r = i
                    attacker_c = j

                # 공격력 낮은 포탐이 두개 이상이라면
                elif board[i][j] == min_blood:
                    # 가장 최근에 공격한 포탑 선정
                    if (i, j) or (attacker_r, attacker_c) in history:
                        for k in range(len(history) - 1, -1, -1):
                            if (i, j) == history[k]:
                                attacker_r = i
                                attacker_c = j
                                break
                            elif (attacker_r, attacker_c) == history[k]:
                                break
                    # 그래도 같으면 행과 열의 합이 가장 큰 포탑
                    elif i + j > attacker_r + attacker_c:
                        attacker_r = i
                        attacker_c = j
                    # 그래도 같으면 열 값이 가장 큰 포탑
                    elif j > attacker_c:
                        attacker_r = i
                        attacker_c = j

    board[attacker_r][attacker_c] += (n + m)
    #history.append((attacker_r, attacker_c))
    return board, attacker_r, attacker_c


def selectVictim(board, attacker_r, attacker_c):
    max_blood = 0
    victim_r = 0
    victim_c = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != 0 and (i,j)!=(attacker_r,attacker_c):
                # 공격력이 가장 높은 포탑 선정
                if max_blood < board[i][j]:
                    victim_r = i
                    victim_c = j
                    max_blood = board[i][j]

                elif max_blood == board[i][j]:
                    # 공격한지 가장 오래된 포탑이 가장 강한 포탑
                    if (i, j) in history or (victim_r, victim_c) in history:

                        for k in range(len(history)):
                            if (i, j) == history[k]:
                                victim_r = i
                                victim_c = j
                                break
                            elif (victim_r, victim_c) == history[k]:
                                break
                    # 그래도 같으면 행과 열의 합이 가장 작은 포탑
                    elif i + j < victim_r + victim_c:
                        victim_r = i
                        victim_c = j
                    # 그래도 같으면 열 값이 가장 작은 포탑
                    elif j < victim_c:
                        victim_r = i
                        attacker_c = j
    history.append((victim_r,victim_c))
    return victim_r, victim_c


def laser(board, attacker_r, attacker_c, victim_r, victim_c):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0] * (m + 1) for _ in range(n + 1)]

    q = deque()
    q.append((attacker_r, attacker_c, []))
    visited[attacker_r][attacker_c] = 1
    power = board[attacker_r][attacker_c]
    prev = {}

    while q:
        x, y, route = q.popleft()
        if x == victim_r and y == victim_c:
            # 역추적
            path = []
            start = (attacker_r, attacker_c)
            end = (victim_r, victim_c)

            at = end
            while at != start:
                path.append(at)
                at = prev[at]

            path.append(start)
            for rx, ry in path:
                if (rx, ry) == (attacker_r, attacker_c): continue
                else:
                    if (rx, ry) == (victim_r, victim_c):
                        board[rx][ry] -= power
                    else:
                        history.append((rx,ry))
                        board[rx][ry] -= power // 2

            board = repair(path, board)

            return board, True

        for i in range(4):
            nx = (x + dx[i]+m) % m
            if nx == 0:
                nx = m
            ny = (y + dy[i]+n) % n
            if ny == 0:
                ny = n
            if isRange(nx, ny):

                if visited[nx][ny] == 1: continue
                if board[nx][ny] == 0: continue
                visited[nx][ny] = 1

                prev[(nx, ny)] = (x, y)
                route.append([nx, ny])
                q.append((nx, ny, route))

    if visited[victim_r][victim_c] == 0:
        return board, False


def repair(arr, board):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) not in arr and board[i][j] != 0:
                board[i][j] += 1
    return board


def checkBroken(board):
    for i in range(n + 1):
        for j in range(m + 1):
            if board[i][j] < 0:
                board[i][j] = 0
    return board


def bomb(board, attacker_r, attacker_c, victim_r, victim_c):
    power = board[attacker_r][attacker_c]
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    board[victim_r][victim_c] -= power
    path = []
    path.append((attacker_r, attacker_c))
    path.append((victim_r, victim_c))
    for i in range(8):
        nx = (victim_r + dx[i]) % m
        ny = (victim_c + dy[i]) % n
        if nx == 0:
            nx = m
        if ny == 0:
            ny = n
        path.append((nx, ny))
        history.append(((nx,ny)))
        board[nx][ny] -= power // 2
    board = checkBroken(board)
    board = repair(path, board)
    return board


def attack(board, attacker_r, attacker_c, victim_r, victim_c):
    board, isattack = laser(board, attacker_r, attacker_c, victim_r, victim_c)

    if isattack:
        board = checkBroken(board)
        return board

    board = bomb(board, attacker_r, attacker_c, victim_r, victim_c)
    return board


for _ in range(k):
    board, attacker_r, attacker_c = selectAttacker(board)

    victim_r, victim_c = selectVictim(board, attacker_r, attacker_c)
    board = attack(board, attacker_r, attacker_c, victim_r, victim_c)
ans = 0
for i in range(1, n + 1):
    if ans < max(board[i]):
        ans = max(board[i])
print(ans)