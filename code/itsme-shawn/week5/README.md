# 5주차

## 1. 백준\_최종순위 (3665)

### 아이디어

1. 작년 순위에서 조합으로 두 개를 꺼내서 인접그래프와 진입차수 설정
2. 올해 바뀐 두 팀 데이터로 인접그래프와 진입차수 갱신
   1. 앞, 뒤가 바뀐 경우 두 가지 모두 고려해야함
3. 진입차수가 0 인 노드 찾아서 그 노드부터 큐에 담고 결과에 저장
4. 도착노드에 진입차수 1씩 감소시키고, 진입차수가 0이 되는 노드는 큐에 저장
5. 4번 반복
6. 결과 리스트의 크기가 팀의 개수이면 정상출력, 아니면 IMPOSSIBLE 출력

### 코드

```python
import sys
from collections import deque
from itertools import combinations

read = sys.stdin.readline

tc = int(read())

for _ in range(tc):
    n = int(read())

    graph = [[0] * (n + 1) for _ in range(n + 1)]  # 인접그래프
    degree = [0] * (n + 1)  # 진입차수
    deq = deque()

    last_ranks = list(map(int, read().split()))

    for a, b in combinations(last_ranks, 2):
        graph[a][b] = 1
        degree[b] += 1

    m = int(read())

    for _ in range(m):
        a, b = map(int, read().split())
        if graph[a][b]:
            graph[a][b] = 0
            degree[b] -= 1
            graph[b][a] = 1
            degree[a] += 1

        elif graph[b][a]:
            graph[b][a] = 0
            degree[a] -= 1
            graph[a][b] = 1
            degree[b] += 1

    for i in range(1, n + 1):
        if degree[i] == 0:
            deq.append(i)

    res = []

    while deq:
        x = deq.popleft()
        res.append(x)
        for i in range(1, n + 1):
            if graph[x][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    deq.append(i)

    if len(res) == n:
        print(*res)
    else:
        print("IMPOSSIBLE")


```

## 2. 백준\_다리 만들기 2 (17472)

### 아이디어

union-find 와 bfs 를 섞은 문제였는데 혼자 힘으로 풀지 못해서 구글링을 통해 코드를 이해했습니다.

bfs_1 : 섬 만들기
bfs_2 : 각 섬의 노드에서 다른 섬으로 가는 다리를 만듦
한 방향으로 진행해야한다는 것이 특이했음
union-find : 사이클 판단

### 코드

```python
# 실패 후 구글링 => 나중에 다시 풀어보기

import sys
from collections import deque

read = sys.stdin.readline

r, c = map(int, read().split())

board = [[0 for _ in range(c)] for _ in range(r)]
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(r)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))  #
edges = []  # 간선 (다리)
island = []  # 섬이 될 수 있는 좌표 (x좌표, y좌표, 섬번호)
visited = [[False for _ in range(c)] for _ in range(r)]


def isin(y, x):
    if -1 < y < r and -1 < x < c:
        return True
    return False


# bfs 로 섬 하나 만들기
def bfs(visited, sy, sx, k):
    q = deque()
    q.append((sy, sx))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if not isin(ny, nx):
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    board[ny][nx] = k
                    q.append((ny, nx))
                    island.append((ny, nx, k))


# 전체 보드판에서 섬 생성
# 전체 보드 순회하면서 조건에 맞을때만 bfs
def make_board():
    visited = [[False for _ in range(c)] for _ in range(r)]
    k = 1
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = True
                board[i][j] = k
                island.append((i, j, k))
                bfs(visited, i, j, k)  # 섬 하나 생성
                k += 1

    return k


# 섬 간 다리 만들기
def make_bridge(sy, sx, k):
    q = deque()

    for dy, dx in d:
        q.append((sy, sx))
        visited = [[False for _ in range(c)] for _ in range(r)]
        visited[sy][sx] = True
        dist = [[0 for _ in range(c)] for _ in range(r)]  # 다리 길이

        while q:
            y, x = q.popleft()

            # 한 방향으로만 직진
            ny = y + dy
            nx = x + dx

            if not isin(ny, nx):
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] == 0:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

                elif board[ny][nx] != k and dist[y][x] >= 2:
                    edges.append((dist[y][x], k, board[ny][nx]))


# union-find
def find_parent(a):
    if parent[a] < 0:
        return a
    parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return False
    parent[b] = a
    return True


n = make_board() - 1
for y, x, k in island:
    make_bridge(y, x, k)
parent = [-1 for _ in range(n + 1)]


edges.sort()
total, cnt = 0, 0

for w, a, b in edges:
    if union_parent(a, b):
        total += w
        cnt += 1
        if cnt == n - 1:
            break
if cnt == n - 1:
    print(total)
else:
    print(-1)


```

## 3. 백준\_어른 상어 (19237)

### 아이디어

구현사항이 많아서 주석으로 정리한 뒤 코드로 옮겼다.

로직 단위 함수로 쪼개고 구현한 뒤, 해당 함수에 오류가 없는지 바로바로 디버깅을 하는 것이 좋다.

```python
# 최초 냄새 뿌리기
# 모든 상어 이동
# 기존 냄새시간 1 감소
# 이동한 곳에 냄새 뿌리기
# 각 상어마다 다음 번에 갈 곳 탐색
# 1. 냄새 없는 곳
# 2. 자신의 냄새
# 후보가 여러 곳이라면 우선순위 방향대로

# 같은 공간에 있는 상어 체크해서 작은 상어만 남김
# 1번 상어만 존재하는지 확인
# 1번만 남아있으면 break
# 다른상어도 있으면 다시 반복
# 1000초 초과하게 되면 -1 출력
```

### 코드

```python
import sys

read = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dx,dy 인덱스 계산 편하게 하기 위해서 맨 앞에 0 삽입
dx.insert(0, 0)
dy.insert(0, 0)

n, m, k = map(int, read().split())  # 격자 길이, 상어 개수, 냄새 지속시간
board = [list(map(int, read().split())) for _ in range(n)]  # 상어의 위치

shark_dist = list(map(int, read().split()))  # 상어의 방향
shark_dist.insert(0, 0)


priority = [[] for _ in range(m + 1)]  # 상어의 방향별 우선순위

for i in range(1, m + 1):
    temp = [list(map(int, read().split())) for _ in range(4)]
    temp.insert(0, [0, 0])  # 인덱스 계산 편하게 하기 위함
    priority[i] = temp

smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
shark_pos = [[0, 0] for _ in range(m + 1)]
# shark_pos[i] : i번째 상어의 위치가 [x,y]

# 상어 위치 담기
for i in range(n):
    for j in range(n):
        if board[i][j]:
            shark_pos[board[i][j]] = [i, j]  # [x좌표, y좌표, 상어번호]


# 디버깅용
def print_smell():
    print("===smell===")
    for row in smell:
        print(row)
    print()


def print_board():
    print("===board===")
    for row in board:
        print(row)
    print()


# 현재 상어 위치에 냄새 뿌리기 함수
def spray():
    for shark_num, [x, y] in enumerate(shark_pos):
        if shark_num == 0 or [x, y] == [-1, -1]:  # 없는 상어 예외처리
            continue
        smell[x][y] = [shark_num, k]


# num번째 상어가 x,y 위치에서 다음 칸으로 이동하는 함수
def move(x, y, num):
    # 현재 상어가 바라보는 방향에 따른 우선순위방향
    priority_dist = priority[num][shark_dist[num]]

    # 아무 냄새가 없는 칸 찾기
    for i in priority_dist:
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and smell[nx][ny] == [0, 0]:
            # 방향 재설정
            shark_dist[num] = i

            # 보드판에 상어 위치 갱신 (삭제, 추가)
            board[x][y] = 0
            board[nx][ny] = num

            # 상어 위치 배열에도 갱신해주기
            shark_pos[num] = [nx, ny]

            return

    # 아무 냄새가 없는 칸이 없는 경우 자신의 냄새가 있는 칸 찾기
    for i in priority_dist:
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and smell[nx][ny][0] == num:
            # 방향 재설정
            shark_dist[num] = i

            board[x][y] = 0
            board[nx][ny] = num

            # 상어 위치 배열에도 갱신해주기
            shark_pos[num] = [nx, ny]
            return


# 보드 전체에서 냄새 감소
def decrease_smell():
    for i in range(n):
        for j in range(n):
            # 냄새 있는 곳 1 감소 시키기
            if smell[i][j][1]:
                smell[i][j][1] -= 1
                # 감소 후에 냄새가 0 이 되면 상어번호도 없애주기
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0


# 한 칸에 상어 겹치는 경우 제일 작은 상어 제외하고 나머지는 삭제
def remove_shark():
    temp = []
    for shark_num, [x, y] in enumerate(shark_pos):
        if shark_num == 0 or [x, y] == [-1, -1]:  # 없는 상어 예외처리
            continue

        if [x, y] not in temp:
            temp.append([x, y])
        else:
            # board 에서 상어 없애고
            board[x][y] = 0

            # shark_pos 에서도 상어위치 없애주기
            shark_pos[shark_num] = [-1, -1]


# 보드판에 1번상어만 남아있는지 체크
def get_is_only_one():
    for shark_num, [x, y] in enumerate(shark_pos):
        if shark_num == 0:
            continue

        # 상어 번호가 1이 아니면서 shark_pos 가 -1,-1 이 아니면 다른 상어가 존재하는 것임
        if shark_num != 1 and [x, y] != [-1, -1]:
            return False
    return True


is_only_one = False
time = 1


while time <= 1000:
    # 최초 냄새 뿌리기
    spray()

    # print_smell()
    # print("===before===")
    # print_board()

    # 모든 상어 이동
    for shark_num, [x, y] in enumerate(shark_pos):
        if shark_num == 0 or [x, y] == [-1, -1]:  # 없는 상어 예외처리
            continue
        move(x, y, shark_num)  # x좌표, y좌표, 상어번호

    # print("===after===")
    # print_board()
    # print_smell()

    # 기존 냄새시간 감소
    decrease_smell()

    # print_smell()

    # 이동한 곳에 냄새 뿌리기
    spray()

    # print_smell()
    # 각 상어마다 다음 번에 갈 곳 탐색

    # 1. 냄새 없는 곳
    # 2. 자신의 냄새
    # 후보가 여러 곳이라면 우선순위 방향대로

    # 같은 공간에 있는 상어 체크해서 작은 상어만 남김
    remove_shark()

    # print_board()

    # 1번 상어만 존재하는지 확인
    is_only_one = get_is_only_one()

    if is_only_one == True:
        break
    else:
        time += 1

    # 1번만 남아있으면 break
    # 다른상어도 있으면 다시 반복
    # 1000초 초과하게 되면 -1 출력

if is_only_one == True:
    print(time)
else:
    print(-1)


# 최초 냄새 뿌리기
# 모든 상어 이동
# 기존 냄새시간 1 감소
# 이동한 곳에 냄새 뿌리기
# 각 상어마다 다음 번에 갈 곳 탐색
# 1. 냄새 없는 곳
# 2. 자신의 냄새
# 후보가 여러 곳이라면 우선순위 방향대로

# 같은 공간에 있는 상어 체크해서 작은 상어만 남김
# 1번 상어만 존재하는지 확인
# 1번만 남아있으면 break
# 다른상어도 있으면 다시 반복
# 1000초 초과하게 되면 -1 출력


```

## 4. 백준\_원판돌리기 (17822)

### 아이디어

1. 해당하는 원판 회전
2. 수평인접체크 (같은 원판)
3. 수직인접체크 (다른 원판 ,같은 위치)
4. 인접하면서 같은 수를 바로 없애는 것이 아니라 다른 자료구조에 저장
5. 2,3번 종료 후 한꺼번에 없애기

### 코드

```python
import sys
from collections import defaultdict, deque

read = sys.stdin.readline


def is_exist_num(circles):
    for value in circles.values():
        for num_lst in value:
            if num_lst[1]:
                return True
    return False


n, m, t = map(int, read().split())
circles = defaultdict(deque)  # 반지름 별 원판에 적힌 숫자
commands = []  # 회전 명령 리스트
for i in range(1, n + 1):
    circle_nums = list(map(int, read().split()))
    deq = deque()
    for j in range(m):
        temp = [circle_nums[j], True]
        deq.append(temp)
    circles[i] += deq

for _ in range(t):
    commands.append(tuple(map(int, read().split())))


# print("initial circle", circles)
# defaultdict(<class 'collections.deque'>, {1: deque([[1, True], [1, True], [2, True], [3, True]]), 2: deque([[5, True], [2, True], [4, True], [2, True]]), 3: deque([[3, True], [1, True], [3, True], [5, True]]), 4: deque([[2, True], [1, True], [3, True], [2, True]])})

for command in commands:
    x, d, k = command  # x : x의배수인 원판선택 / d : 0(시계),1(반시계) / k : 회전횟수

    for radius, nums in circles.items():
        if radius % x == 0:
            if d == 0:
                nums.rotate(k)
            else:
                nums.rotate(-k)

    # print(circles)

    is_exist = is_exist_num(circles)
    is_delete = False  # 인접한 수 지웠는지 체크하는 플래그 변수

    # 원판에 수가 남아있는 경우
    if is_exist:
        # 수평인접 (같은 원판)
        for nums in circles.values():
            # print("수평인접 before", nums)
            # ex) deque([[2, True], [5, True], [2, True], [4, True]])
            if len(nums) >= 2:
                i, j = 0, 1
                while i <= len(nums) - 2 and j <= len(nums) - 1:
                    if nums[i][0] and nums[j][0] and nums[i][0] == nums[j][0]:
                        nums[i][1] = False
                        nums[j][1] = False
                        is_delete = True
                    i += 1
                    j += 1
                # 마지막 원소 처리
                if nums[0][0] and nums[-1][0] and nums[0][0] == nums[-1][0]:
                    nums[0][1] = False
                    nums[-1][1] = False
                    is_delete = True
            # print("수평인접체크 after", nums)

        # 수직인접 (다른 원판인데 같은 위치)
        verticals = [[] for _ in range(m)]
        for nums in circles.values():
            for i in range(len(nums)):
                verticals[i] += [nums[i]]

        # print("수직인접 before", verticals)

        for vertical in verticals:
            if len(vertical) >= 2:
                i, j = 0, 1
                while i <= len(vertical) - 2 and j <= len(vertical) - 1:
                    if vertical[i][0] and vertical[j][0] and vertical[i][0] == vertical[j][0]:
                        vertical[i][1] = False
                        vertical[j][1] = False
                        is_delete = True
                    i += 1
                    j += 1
            # print("수직인접 after", vertical)

        # print("after 수평,수직 체크", circles)

        # 인접하면서 같은 수가 있는 경우 (지워야 할 숫자가 있는 경우)
        if is_delete:
            for value in circles.values():
                for num_lst in value:
                    if not num_lst[1]:
                        num_lst[0] = 0  # 삭제한다는 의미
        # 인접하면서 같은 수가 없는 경우
        else:
            total = 0
            cnt = 0
            for value in circles.values():
                for num_lst in value:
                    if num_lst[1]:
                        total += num_lst[0]
                        cnt += 1
            aver = total / cnt
            # print("aver", aver)

            for value in circles.values():
                for num_lst in value:
                    if num_lst[1]:  # 이거 추가했어야함
                        if num_lst[0] > aver:
                            num_lst[0] -= 1
                        elif num_lst[0] < aver:
                            num_lst[0] += 1

        # print("회전 후 최종 원판", circles)
        # print("is_delete", is_delete)


# 최종 계산
total = 0
for value in circles.values():
    for num_lst in value:
        if num_lst[1]:
            total += num_lst[0]

print(total)


```
