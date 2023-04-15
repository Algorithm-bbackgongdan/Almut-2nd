from collections import deque


def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)
    MAX = int(1e9)

    def bfs(start):
        visited = [[MAX] * n for _ in range(n)]
        visited[0][0] = 0

        q = deque([start])  # x, y, cost, direction
        while q:
            x, y, c, d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    # dp

                    if i == d:  # 방향 그대로이면 직선 금액 계산
                        nc = c + 100
                    else:  # 방향 달라지면 코너 금액 계산
                        nc = c + 600

                    # new cost 가 작을 때만 갱신하고 방문처리, 큐 append
                    if nc < visited[nx][ny]:
                        visited[nx][ny] = nc
                        q.append([nx, ny, nc, i])

        return visited[n - 1][n - 1]

    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])
