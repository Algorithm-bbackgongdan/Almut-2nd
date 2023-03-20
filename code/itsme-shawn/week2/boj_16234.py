import sys

sys.setrecursionlimit(10**8)

read = sys.stdin.readline

n, L, R = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:  # 미방문노드면
                if L <= abs(board[nx][ny] - board[x][y]) <= R:
                    visited[nx][ny] = 1
                    stack.append([nx, ny])
                    dfs(nx, ny)


move_day = 0

while True:
    flag = 0
    visited = [[0] * n for _ in range(n)]

    # 전체 board에 대해 dfs & 인구이동 (1일)
    for i in range(n):
        for j in range(n):
            stack = []
            if visited[i][j] == 0:  # 방문 안 한 노드만 dfs
                visited[i][j] = 1
                stack.append([i, j])
                dfs(i, j)

                # 한 지점에 대해 dfs 완료하면, 국경선을 열고 인구이동 시킴
                if len(stack) > 1:
                    flag = True
                    avg = sum([board[x][y] for x, y in stack]) // len(stack)
                    for x, y in stack:
                        board[x][y] = avg

    if flag == 0:
        break

    move_day += 1

print(move_day)
