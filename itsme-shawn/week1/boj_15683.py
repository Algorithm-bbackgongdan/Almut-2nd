import copy
import sys
from itertools import product

read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# n, m : 사무실 세로 / 가로
# i, j  : CCTV 현재 위치
def watch(board, n, m, direction, i, j):
    nx, ny = i, j
    if direction == 0:
        for _ in range(i):
            nx += dx[0]
            if 1 <= board[nx][ny] <= 5:
                continue
            elif board[nx][ny] == 6:
                break
            board[nx][ny] = -1

    if direction == 1:
        for _ in range(m - (j + 1)):
            ny += dy[1]
            if 1 <= board[nx][ny] <= 5:
                continue
            elif board[nx][ny] == 6:
                break
            board[nx][ny] = -1

    if direction == 2:
        for _ in range(n - (i + 1)):
            nx += dx[2]
            if 1 <= board[nx][ny] <= 5:
                continue
            elif board[nx][ny] == 6:
                break
            board[nx][ny] = -1

    if direction == 3:
        for _ in range(j):
            ny += dy[3]
            if 1 <= board[nx][ny] <= 5:
                continue
            elif board[nx][ny] == 6:
                break
            board[nx][ny] = -1


def cctv(c_type):
    if c_type == 1:
        return [[0], [1], [2], [3]]
    if c_type == 2:
        return [[1, 3], [0, 2]] * 2
    if c_type == 3:
        return [[0, 1], [1, 2], [2, 3], [3, 0]]
    if c_type == 4:
        return [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    if c_type == 5:
        return [[0, 1, 2, 3]] * 4


n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]


cctv_cnt = 0
cctv_location = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            cctv_location.append((i, j))
            cctv_cnt += 1

minn = 10e9

directions = []
cctv_lst = []
for i, j in cctv_location:
    c_type = board[i][j]
    direction = cctv(c_type)
    directions.append(direction)

minn = 10e9

for p in product(*directions):
    cur = 0
    new_board = copy.deepcopy(board)
    for i, directions in enumerate(p):
        for direction in directions:
            watch(new_board, n, m, direction, cctv_location[i][0], cctv_location[i][1])
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                cur += 1
    minn = min(minn, cur)

print(minn)
