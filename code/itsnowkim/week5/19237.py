# 어른 상어
n,m,k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 각 상어의 방향, index 맞추기
current_direction = list(map(int, input().split()))
current_direction = [x-1 for x in current_direction]

current_xy = [[]for _ in range(m)]
# 현재 보드에 존재하는 모든 상어의 좌표를 구하고 시작
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            idx = board[i][j]
            current_xy[idx-1] = [i,j]
            board[i][j] = [idx-1,k]
# 방향 인덱스와 순서 맞춰서 선언
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# 방향 우선순위 존재 - 상어 하나당 4개씩,
# 위 아래 왼쪽 오른쪽 순서로 입력받음
shark_table = []
for i in range(m):
    temp = {}
    for j in range(4):
        # 읽고, index 맞춰주기
        data = list(map(int,input().split()))
        temp[j] = [x-1 for x in data]
        
    shark_table.append(temp)

# 남아있는 상어 마리 수
remain_shark = m

def move_shark(idx, curr_x, curr_y):
    """
    1. 상어의 우선순위 방위대로 이동한다.(상어의 현재 위치만 업데이트)
    """
    # 현재 바라보고 있는 방향
    curr_dir = current_direction[idx]
    # 상어의 우선순위 방향대로 순회
    for dir in shark_table[idx][curr_dir]:
        x,y = directions[dir]
        nx = curr_x + x
        ny = curr_y + y
        if 0<= nx and nx<n and 0<=ny and ny<n:
            if board[nx][ny] == 0: # 빈 공간일 경우
                # 현재 위치 업데이트
                current_xy[idx]=[nx, ny]
                # 방향 업데이트
                current_direction[idx] = dir

                # nx, ny로 이동, 마스킹 -> 마스킹은 맨 마지막에 해야 함. 모든 상어는 동시에 움직이기 때문.
                # board[nx][ny] = [idx,k+1]
                return  (idx, nx,ny)

    # 본인의 영역 확인, 우선순위 방위대로 이동
    for dir in shark_table[idx][curr_dir]:
        x,y = directions[dir]
        nx = curr_x + x
        ny = curr_y + y
        if 0<= nx and nx<n and 0<=ny and ny<n:
            if board[nx][ny] != 0 and board[nx][ny][0]==idx:
                # 현재 위치 업데이트
                current_xy[idx]=[nx,ny]
                # 방향 업데이트
                current_direction[idx] = dir
                # nx, ny로 이동, 마스킹.
                # board[nx][ny] = [idx,k+1]
                return  (idx,nx,ny)

def update_board():
    """
    1. 보드에 존재하는 모든 채취의 지속시간을 -1한다.
    2. 만약 0이 되는 case에는 0으로 만든다.
    """
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                if board[i][j][1] == 1: # 지속시간이 0이 될 때 빈 보드로 만들기
                    board[i][j] = 0
                else:
                    board[i][j][1] -= 1 # 지속시간 -1

def check_who_out():
    """
    1. 같은 좌표에 올라간 상어를 체크한다.
    2. 해당 격자에 가장 낮은 상어만 남기고, 그 외의 상어는 없앤다.
    """
    will_out = []
    # print('current xy : ',current_xy)
    # 첫 번째 상어부터 순서대로 확인
    for i in range(0, remain_shark-1):
        curr_x,curr_y = current_xy[i]
        for j in range(i+1,remain_shark):
            x,y = current_xy[j]
            if (curr_x, curr_y)==(x,y):# 같은 좌표에 올라가 있는 경우, 뒷 인덱스의 상어는 쫓겨난다.
                will_out.append(j)
    
    return will_out

def masking_area(movement_list):
    """
    같은 좌표에 같이 마스킹을 할 수 없다.
    무조건 idx가 작은 상어의 masking만 남도록.
    """
    movement_list.sort(reverse=True)
    for idx, nx, ny in movement_list:
        board[nx][ny] = [idx, k+1]

# 1번 상어만 격자에 남게 되기까지 걸리는 시간 출력
for time in range(1, 1002):
    # 1000초가 넘는 경우, -1출력
    if time > 1000:
        print(-1)
    
    # step1: 모든 상어는 동시에 이동한다.
    new_movement = []
    for idx, xy in enumerate(current_xy):
        curr_x, curr_y = xy
        if curr_x != -1 and curr_y!= -1:
            temp = move_shark(idx, curr_x, curr_y)
            if temp:
                new_movement.append(temp)

    # 영역 남기는 함수
    masking_area(new_movement)
    # 이동 후 보드 업데이트
    update_board()

    # 겹치는 상어를 체크하고, 가장 작은 상어만 남긴다.
    out_list = check_who_out()

    # 리스트에 있는 상어 제거
    for i in out_list:
        current_xy[i] = [-1,-1]
        current_direction[i] = -1
        remain_shark -= 1

    # 만약 상어가 한 마리만 남은 경우, 종료한다.
    if remain_shark == 1:
        print(time)
        break
    