from collections import deque

DOWN = 0
RIGHT = 1
UP = 2
LEFT = 3

STRAIGHT_FEE = 100
CORNER_FEE = 600

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def solution(board):
    n = len(board)
    queue = deque([])  # 위치, 방향
    costs = [
        [[float("inf"), float("inf"), float("inf"), float("inf")] for _ in range(n)]
        for _ in range(n)
    ]  # cost[i][j][k]: board(i, j)로 k 방향으로 갈 때 최소 비용

    # 출발점에 대해 비용 초기화
    for dir in range(4):
        costs[0][0][dir] = 0

    # 출발점에서는 오른쪽, 아래로만 움직일 수 있음
    queue.append(((0, 0), RIGHT))
    queue.append(((0, 0), DOWN))

    while queue:
        curPos, curDir = queue.popleft()

        curX, curY = curPos
        curFee = costs[curX][curY][curDir]

        if curPos == (n - 1, n - 1):
            continue

        # 인접한 방향에 대해
        for newDir, dir in enumerate(DIRECTIONS):
            dirX, dirY = dir
            newX, newY = curX + dirX, curY + dirY

            if newX < 0 or newX >= n or newY < 0 or newY >= n or board[newX][newY] == 1:
                continue

            # 현재 방향과 새로운 방향이 같으면 직선, 아니면 코너
            newCost = curFee + STRAIGHT_FEE if curDir == newDir else curFee + CORNER_FEE

            # 비용이 갱신되면 큐에 추가
            if newCost <= costs[newX][newY][newDir]:
                costs[newX][newY][newDir] = newCost
                queue.append(((newX, newY), newDir))

    return min(costs[n - 1][n - 1])
