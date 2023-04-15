from collections import deque

INF = int(1e10)


def bfs(board, cost, N):
    global answer
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cost[0][0][0] = cost[1][0][0] = 0
    q = deque([(0, 0, 0)])
    q = deque([(0, 0, 1)])
    while q:
        y, x, d = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nd = i
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                c = cost[d][y][x] + 100
                if (x, y) != (0, 0) and nd != d:
                    c += 500
                if c < cost[nd][ny][nx]:
                    cost[nd][ny][nx] = c
                    if ny == N - 1 and nx == N - 1:
                        answer = min(answer, c)
                    else:
                        q.append((ny, nx, nd))


def solution(board):
    global answer
    answer = INF
    N = len(board)
    cost = [[[INF] * N for _ in range(N)] for _ in range(4)]
    bfs(board, cost, N)
    return answer
