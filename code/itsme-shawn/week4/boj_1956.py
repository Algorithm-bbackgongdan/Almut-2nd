import sys

read = sys.stdin.readline

V, E = map(int, read().split())
MAX = 1e9
dis = [[MAX] * (V + 1) for _ in range(V + 1)]  # 2차원배열 초기화

# 그래프 생성
for i in range(E):
    a, b, c = map(int, read().split())  # a : 시작노드, b : 도착노드, c : 가중치
    dis[a][b] = c

# 플로이드-와샬
for k in range(1, V + 1):  # k : 중간노드
    for i in range(1, V + 1):  # i : 시작노드(행)
        for j in range(1, V + 1):  # j : 도착노드(열)
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

# 출력
ans = MAX
for i in range(V + 1):
    ans = min(ans, dis[i][i])  # dis[i][i] : 사이클 (시작점 ~ 시작점)


if ans == 1e9:  # 최소값이 없으면 -1 출력
    print(-1)
else:
    print(ans)
