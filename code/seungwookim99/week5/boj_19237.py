import sys

input = sys.stdin.readline

# static variables
NULL = -1
DIRECTION, COORDINATE = 0, 1
NUMBER, TIME = 0, 1
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
dy = [NULL] + [-1, 1, 0, 0]
dx = [NULL] + [0, 0, -1, 1]

# variables
time = 0

# inputs
n, m, k = map(int, input().split())
sharks = [NULL] * (m + 1)
outs = [False] * (m + 1)

B = []
for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 0:
            tmp[x] = [tmp[x], -k]
            continue
        sharks[tmp[x]] = [NULL, (y, x)]  # (현재 방향, 현재 좌표)
        tmp[x] = [tmp[x], 0]  # (상어 번호, 냄새 뿌린 시각)
    B.append(tmp)

dirs = [NULL] + list(map(int, input().split()))
for i in range(1, m + 1):
    sharks[i][DIRECTION] = dirs[i]

priorities = [[NULL] * 5 for _ in range(m + 1)]

for i in range(1, m + 1):
    for dir in [UP, DOWN, LEFT, RIGHT]:
        priorities[i][dir] = list(map(int, input().split()))


# start
def only_number_one_left():
    for i in range(2, m + 1):
        if not outs[i]:
            return False
    return not outs[1]


def inside_boundary(y, x):
    return (0 <= y < n) and (0 <= x < n)


def is_no_scent(y, x):
    return B[y][x][TIME] + k <= time


def is_my_scent(y, x, num):
    return B[y][x][NUMBER] == num


def get_next_cell(num, coordinate, prior):
    (y, x) = coordinate
    no_scents, my_scents = [], []
    for dir in prior:
        ny, nx = y + dy[dir], x + dx[dir]
        if not inside_boundary(ny, nx):
            continue
        if is_no_scent(ny, nx):
            no_scents.append((ny, nx, dir))
        elif is_my_scent(ny, nx, num):
            my_scents.append((ny, nx, dir))

    if len(no_scents) > 0:
        return no_scents[0]
    else:
        return my_scents[0]


def move(next_cells):
    for num in range(1, m + 1):
        if next_cells[num] == NULL:
            continue
        (ny, nx, ndir) = next_cells[num]
        if is_no_scent(ny, nx) or is_my_scent(ny, nx, num):
            B[ny][nx][NUMBER] = num
            B[ny][nx][TIME] = time + 1
            sharks[num][DIRECTION] = ndir
            sharks[num][COORDINATE] = (ny, nx)
        else:
            outs[num] = True
            sharks[num] = (NULL, (NULL, NULL))
    return


while time <= 1000 and not only_number_one_left():
    next_cells = [NULL] * (m + 1)
    for num in range(1, m + 1):
        if outs[num]:
            continue
        direction, coordinate = sharks[num]
        prior = priorities[num][direction]
        # 다음으로 이동할 위치 구한 뒤 저장
        (ny, nx, ndir) = get_next_cell(num, coordinate, prior)
        next_cells[num] = (ny, nx, ndir)

    # 실제 이동 처리
    move(next_cells)
    time += 1

if time == 1001:
    print(-1)
else:
    print(time)
