import sys
from collections import deque

def check_boundary(y, x):
    return 0 <= y < N and 0 <= x < N


def check_moveable(a, b):
    return L <= abs(a - b) <= R


def move():
    # unions에 저장된 정보를 바탕으로 인구이동 처리
    for (contries, population) in unions:
        for (y, x) in contries:
            world[y][x] = population


def union_exist(y, x):
    # (y,x)을 시작으로 연합국가가 존재하는지 bfs로 체크
    # 존재하면 (연합국가들의 좌표 리스트, 인구수 평균) 을 unions에 append 후 True 반환
    # 존재하지 않으면 False 반환
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    q = deque([(y, x)])
    contries = []
    populationSum = 0
    visited[y][x] = True

    while q:
        cy, cx = q.popleft()
        contries.append((cy, cx))
        populationSum += world[cy][cx]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if check_boundary(ny,nx) and not visited[ny][nx] and check_moveable(world[cy][cx], world[ny][nx]):
                visited[ny][nx] = True
                q.append((ny, nx))

    populationAvg = populationSum // len(contries)
    if len(contries) == 1:
        return False
    else:
        unions.append((contries, populationAvg))
        return True


N, L, R = map(int, sys.stdin.readline().rstrip().split(' '))
world = [ list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

days = 0
moveCanOccur = True

while moveCanOccur:
    moveCanOccur = False
    visited = [[False] * N for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and union_exist(i, j):
                moveCanOccur = True
    if moveCanOccur:
        move()
        days += 1
print(days)
