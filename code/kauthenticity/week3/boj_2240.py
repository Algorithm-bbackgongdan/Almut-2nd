import sys

t, w = map(int, sys.stdin.readline().split())
targetTrees = list(int(sys.stdin.readline().strip()) for _ in range(t))


def solution(t, w, targetTrees):
    # dp[i][j] i초에서 j번 움직였을 떄 얻을 수 있는 최대 사과 개수
    dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)]

    # targetTrees[i]: i초에 나무 정보
    # 0초에 대한 정보도 추가해준다.
    targetTrees = [0] + targetTrees

    for i in range(1, t + 1):
        # 한번도 안 움직이고 쭉 1번에 있는 경우
        dp[i][0] = dp[i - 1][0] + 1 if targetTrees[i] == 1 else dp[i - 1][0]

        for j in range(1, min(w + 1, i + 1)):
            currentTree = 1 if j % 2 == 0 else 2
            score = 1 if targetTrees[i] == currentTree else 0

            # i-1초에서 그대로 있는 경우, i-1초의 위치에서 자리를 바꾼 경우
            # 둘 중 큰 값
            dp[i][j] = max(dp[i - 1][j] + score, dp[i - 1][j - 1] + score)

    return max(dp[t])


print(solution(t, w, targetTrees))
