# 경주로 건설

from collections import deque

def in_board(x, y, N):
    if 0<=x and x<N and 0<=y and y<N:
        return True
    return False

def solution(board):
    # 무한 초기화
    INF = int(1e9)
    # 보드 길이는 n*n
    N = len(board)
    # 방향 배열 - 처음 방향은 오른쪽으로 가거나, 아래로 가거나 둘 중 하나
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # cost 배열
    costmap = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)]
    costmap[0][0][0] = 0
    costmap[1][0][0] = 0
    costmap[2][0][0] = 0
    costmap[3][0][0] = 0

    # q 초기화 - (x, y, cost, direction)
    q = deque([(0, 0, 0, 1), (0, 0, 0, 3)])

    while q:
        curr_x, curr_y, curr_cost, curr_dir = q.popleft()

        for dir_index, dir in enumerate(directions):
            x, y = dir
            nx, ny = curr_x+x, curr_y+y

            # 보드 내에 존재하며, 이동할 수 있는 경우만 고려
            if in_board(nx, ny, N) and board[nx][ny] == 0:
                new_cost = curr_cost+100
                if curr_dir!=dir_index: # 방향이 다른 경우 500 추가
                    new_cost += 500
                
                # 업데이트할지, 말지 결정
                if new_cost < costmap[dir_index][nx][ny]:
                        q.append((nx, ny, new_cost, dir_index))
                        costmap[dir_index][nx][ny] = new_cost
                
    return min([costmap[0][N-1][N-1],costmap[1][N-1][N-1],costmap[2][N-1][N-1],costmap[3][N-1][N-1]])
    

# print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 900
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])) # 3800
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) #2100
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])) #3200