import sys

read = sys.stdin.readline

T, W = map(int, read().split())
trees = [int(read()) for _ in range(T)]

dp = [[[0 for i in range(3)] for j in range(31)] for k in range(1001)]  # dp[시간][이동횟수][위치] => 1001 * 31 * 3

dp[0][0][1] = 0
dp[0][0][2] = 0

res = 0

for time in range(T):
    for cnt in range(W + 1):  # 0 : 이동X
        if trees[time] == 1:  # 1번 위치에 자두가 떨어질 때
            if cnt == 0:
                dp[time][cnt][1] = dp[time - 1][cnt][1] + 1  # 제자리(1번위치)에서 이동 안 하는 경우
            else:
                dp[time][cnt][1] = max(dp[time - 1][cnt][1], dp[time - 1][cnt - 1][2]) + 1
                dp[time][cnt][2] = max(dp[time - 1][cnt - 1][1], dp[time - 1][cnt][2])
                res = max(dp[time][cnt][1], dp[time][cnt][2])
        else:  # 2번 위치에 자두가 떨어질 때
            if cnt == 0:
                dp[time][cnt][1] = dp[time - 1][cnt][1]  # 제자리(1번위치)에서 이동 안 하는 경우
            else:
                dp[time][cnt][1] = max(dp[time - 1][cnt][1], dp[time - 1][cnt - 1][2])
                dp[time][cnt][2] = max(dp[time - 1][cnt - 1][1], dp[time - 1][cnt][2]) + 1
                res = max(dp[time][cnt][1], dp[time][cnt][2])

print(res)
