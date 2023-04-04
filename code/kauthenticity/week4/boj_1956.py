from sys import stdin


def solution(v, e, dists):
    answer = float("inf")

    # 플로이드 워셜
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                newDist = dists[i][k] + dists[k][j]
                if dists[i][j] > newDist:
                    dists[i][j] = newDist

    # 최소 사이클을 찾는다
    for i in range(1, v + 1):
        for j in range(1, i):
            answer = min(answer, dists[i][j] + dists[j][i])

    return -1 if answer == float("inf") else answer


v, e = map(int, stdin.readline().split())

# 그래프의 cost는 무한으로 초기화
dists = [[float("inf") for _ in range(v + 1)] for _ in range(v + 1)]

for _ in range(e):
    v1, v2, cost = map(int, stdin.readline().split())
    dists[v1][v2] = cost

print(solution(v=v, e=e, dists=dists))
