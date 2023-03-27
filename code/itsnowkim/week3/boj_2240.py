T, W = map(int, input().split())
array = []
for i in range(T):
    array.append(int(input()))
array = [0] + array

dp = [[0 for _ in range(W + 1)] for _ in range(T+1)]

# dp[i][j] -> i 초에 j번 이동했을 때 먹는 자두 개수
for i in range(1, T+1):
    # 맨 첫 줄 초기화
    if array[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    
    for j in range(1, min(W+1, i+1)):
        # 지금까지 움직인 횟수에 따른 현재 위치
        if j%2 == 0:
            curr = 1
        else:
            curr = 2
        
        # 현재 위치에 따른 자두 획득
        if array[i] == curr:
            score = 1
        else:
            score = 0

        dp[i][j] = max(dp[i-1][j] + score, dp[i-1][j-1] + score)

print(max(dp[T]))