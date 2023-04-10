from sys import stdin

DIRECTIONS = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


def moveShark(deadSharks):
    newBoard = [[0 for _ in range(n)] for _ in range(n)]
    sharkMoves = []  # shark number, shark direction, x, y
    deadSharkNum = 0

    # 상어가 움직일 수 있는 방향을 구함
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue

            sharkNumber = board[i][j]
            sharkDirection = directions[sharkNumber]
            curPriority = priorities[sharkNumber][sharkDirection]
            foundDirection = False

            # 우선순위대로 돌면서 움직일 수 있는 지 확인
            for priority in curPriority:
                dirX, dirY = DIRECTIONS[priority]
                newX, newY = i + dirX, j + dirY

                if newX < 0 or newX >= n or newY < 0 or newY >= n:
                    continue

                # 우선순위대로 움직였는데 냄새가 안 남
                if len(smell[newX][newY]) == 0:
                    foundDirection = True
                    sharkMoves.append((sharkNumber, priority, newX, newY))
                    break

            # 자기 냄새로 이동할 수 있는지 우선순위 순서대로 확인
            if not foundDirection:
                for priority in curPriority:
                    dirX, dirY = DIRECTIONS[priority]
                    newX, newY = i + dirX, j + dirY

                    if newX < 0 or newX >= n or newY < 0 or newY >= n:
                        continue

                    if smell[newX][newY][0] == sharkNumber:
                        sharkMoves.append((sharkNumber, priority, newX, newY))
                        break

    for i in range(n):
        for j in range(n):
            if len(smell[i][j]) == 0:
                continue

            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

    # 상어를 움직임
    for sharkNumber, sharkDirection, newX, newY in sharkMoves:
        if newBoard[newX][newY] == 0:
            newBoard[newX][newY] = sharkNumber
            directions[sharkNumber] = sharkDirection
            smell[newX][newY] = [sharkNumber, k]
        else:
            newBoard[newX][newY] = min(sharkNumber, newBoard[newX][newY])
            smell[newX][newY] = [newBoard[newX][newY], k]
            directions[sharkNumber] = sharkDirection
            deadSharkNum += 1

    return deadSharkNum, newBoard


def solution():
    global board
    answer = 0

    deadSharks = []
    deadSharkNum = 0
    t = 0

    while t < 1000:
        if deadSharkNum == m - 1:
            break

        curDeadSharkNum, board = moveShark(deadSharks)
        deadSharkNum += curDeadSharkNum

        t += 1

    answer = t

    return answer


n, m, k = map(int, stdin.readline().split())  # n: 격자 크기, m: 상어 개체 수, k: 몇 초 후에 냄새가 사라질지

board = [list(map(int, stdin.readline().split())) for _ in range(n)]

directions = [0]
directions.extend(
    list(map(int, stdin.readline().split()))
)  # directions[i]: i번 상어가 보고있는 방향. 1: 상, 2: 하, 3: 좌, 4: 우
priorities = [[]]  # priorities[i][j]: i번 상어가 j번 방향을 바라볼 때 우선 순위

for i in range(m):
    curPriority = [[]]
    curPriority.extend([list(map(int, stdin.readline().split())) for _ in range(4)])
    priorities.append(curPriority)

smell = [
    [[] for _ in range(n)] for _ in range(n)
]  # smell[i][j]: (i, j)위치의 (냄새의 주인, 냄새가 없어지기까지 남은 시간)
print(solution())
