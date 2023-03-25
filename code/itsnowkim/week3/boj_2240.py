def turn(num):
    if num == 1:
        return 2
    else:
        return 1

T, W = map(int, input().split())
array = []
for i in range(T):
    array.append(int(input()))

# dp table
dp = []
sol = []
for i in range(W+1):
    dp.append([[0,0]]*(T))
    sol.append([0]*T)

# 0번째 초기화
for i in range(1, T):
    dp[0][i][0] = 1 # 현재 위치
    dp[0][i][1] = 0 # 지금까지 이동 횟수
    
    if array[i] == 1:
        sol[0][i] = sol[0][i-1] + 1
    else:
        sol[0][i] = sol[0][i-1]

# 이동횟수 1부터 dp 테이블 작성
for i in range(1, W):
    pos = 1
    for j in range(T):
        if array[j] == 1 and j%2 == 0:
            sol[i][j] = max(sol[i-1][j], sol[i-1][j-1]) + 1
        elif array[j] == 2 and j%2 == 1:
            sol[i][j] = max(sol[i-1][j], sol[i-1][j-1]) + 1
        else:
            sol[i][j] = max(dp[i-1][j],dp[i-1][j-1])

print(sol[W][-1])


            
                

