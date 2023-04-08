import sys
from collections import deque

n,m,t = map(int,input().split()) #원판의 개수, 원판에 적힌 정수의 개수, T 번 회전
board = [deque(int(x) for x in input().split()) for _ in range(n)]
info = [[int(x) for x in input().split()] for _ in range(t)] # x배수, d 방향, k 칸 회전
# d == 0 시계 방향 d == 1 반시계 방향

for tc in range(t):
    x,d,k = info[tc]
    # 회전하기
    result = 0
    for i in range(n):
        result += sum(board[i])
        if (i+1)%x == 0:
            if d == 0:
                board[i].rotate(k)
            else:
                board[i].rotate(-k)
    
    # 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다
    if result != 0:
        #그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
        have_to_remove = []
        # 먼저 같은 원내에서 인접한 애들
        for i in range(n):
            for j in range(m-1):
                if board[i][j] != 0 and board[i][j+1] != 0 and board[i][j] == board[i][j+1]:
                    have_to_remove.append((i,j))
                    have_to_remove.append((i,j+1))
            if board[i][0] != 0 and board[i][-1]!=0 and board[i][0] == board[i][-1]:
                have_to_remove.append((i,0))
                have_to_remove.append((i,m-1))

        # 옆의 원
        for j in range(m):
            for i in range(n-1):
                if board[i][j] != 0 and board[i+1][j] != 0 and board[i][j] == board[i+1][j]:
                    have_to_remove.append((i,j))
                    have_to_remove.append((i+1,j))

        # 원판 다시 만들어주기
        have_to_remove = list(set(have_to_remove))

        for i in range(len(have_to_remove)):
            x,y = have_to_remove[i]
            board[x][y] = 0

        #없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
        if len(have_to_remove) == 0:
            avg_sum = 0
            zero_cnt = 0
            for i in range(n):
                avg_sum += sum(board[i])
                zero_cnt += board[i].count(0)
            avg = avg_sum / (n*m-zero_cnt)

            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0 and  board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] !=0 and board[i][j] < avg:
                        board[i][j] += 1
    else:
        break

ans = 0
for i in range(n):
    ans += sum(board[i])

print(ans)