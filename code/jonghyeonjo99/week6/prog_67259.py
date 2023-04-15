from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(board):
    global now_cost
    queue = deque()
    answer = 1e9
    costs = [[[1e9] * len(board) for i in range(len(board))] for _ in range(4)]

    for i in range(4):
      costs[i][0][0] = 0

    if board[0][1] == 0:
      queue.append([0,1,100,0])
      costs[0][0][1] = 100

    if board[1][0] == 0:
      queue.append([1,0,100,1])
      costs[1][1][0] = 100

    while queue:
        x,y,cost,dir = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] == 1:
                    continue
                if(dir == -1 or dir == i): 
                    now_cost = cost + 100
                else: 
                    now_cost = cost + 600

                if costs[i][nx][ny] > now_cost:
                    costs[i][nx][ny] = now_cost
                    queue.append([nx,ny,now_cost,i])
    return min([costs[i][-1][-1] for i in range(4)])