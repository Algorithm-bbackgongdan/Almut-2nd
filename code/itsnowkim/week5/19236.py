# 청소년 상어
import copy

array = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        array[i][j] = [data[(j*2)], data[(j*2)+1]-1]

# 방향에 대한 정의 - 반시계 순으로 정의
directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

# 상어가 먹은 물고기 총합
answer = 0

# 순서가 빠른 것부터 좌표 리턴
def get_fish_position(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None # 해당 물고기 없음

# 전체 물고기 이동하기
def move_fishes(array,curr_x,curr_y):
    # 순서대로 물고기 이동
    for i in range(1,17):
        position = get_fish_position(array, i)
        if position != None:
            # 물고기 위치와 방향 구하기
            x, y = position
            dir = array[x][y][1]
            # 이동 가능한지 탐색 - 8방향이므로 8번만 체크
            for j in range(8):
                # 가려는 방향
                tx,ty = directions[dir]
                nx = x+tx
                ny = y+ty
                # 존재하는 보드이며, 상어가 없을 경우 서로의 위치 변경
                if 0<=nx and nx <4 and 0<=ny and ny<4:
                    if (nx,ny)!=(curr_x,curr_y):
                        temp = array[nx][ny]
                        array[nx][ny] = array[x][y]
                        array[x][y] = temp
                        break
                # 이동을 못한 경우임. 방향전환 필요
                dir = (dir+1)%8

# 상어의 이동
# 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def possible_fishes(array, x, y):
    dir_index = array[x][y][1]
    tx,ty = directions[dir_index]

    res = []
    # 가능한 위치로 이동해보기 - 최대 이동 가능한 거리는 3칸
    for i in range(4):
        x += tx
        y += ty
        if 0<=x and x<4 and 0<= y and y<4:
            if array[x][y][0] != -1: # 먹이가 있다는 뜻
                res.append((x,y))
    return res

def dfs(array, now_x, now_y, total):
    global answer
    array = copy.deepcopy(array) # 리스트를 통째로 복사

    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1 # 물고기를 먹었으므로 -1로 변환

    move_fishes(array, now_x, now_y) # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례
    positions = possible_fishes(array, now_x, now_y)
    # 종료 조건 - 상어가 이동할 수 있는 방향에 있는 모든 칸이 빈 물고기인 경우
    if len(positions) == 0:
        answer = max(answer, total)
        return
    
    # 재귀적으로 이동하면서 먹기
    for next_x, next_y in positions:
        dfs(array,next_x, next_y, total)

dfs(array,0,0,0)
print(answer)


