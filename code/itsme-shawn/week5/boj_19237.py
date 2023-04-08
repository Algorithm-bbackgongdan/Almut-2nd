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
