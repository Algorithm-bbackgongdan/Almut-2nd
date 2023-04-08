from sys import stdin
from collections import deque


def getInput():
    n = int(input())
    ranks = list(map(int, stdin.readline().split()))
    m = int(input())

    changes = [list(map(int, stdin.readline().split())) for _ in range(m)]

    return n, ranks, m, changes


def makeRanksToGraph(ranks, n):
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]

    for i in range(len(ranks) - 1):
        cur = ranks[i]
        for j in range(i + 1, len(ranks)):
            next = ranks[j]
            graph[cur][next] = True
            indegree[next] += 1

    return graph, indegree


def getRank(graph, indegree, n):
    answer = []
    queue = deque([])

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 최소한 n번 돌아서 확인해야 함.
    for i in range(n):
        if not queue:
            return "IMPOSSIBLE"

        if len(queue) > 0:
            return "?"

        cur = queue.popleft()
        answer.append(cur)

        # 현재 노드를 포함하는 edge를 없앰
        for next in range(1, n + 1):
            indegree[next] -= 1

            # indegree가 0인 노드를 큐에 넣어서 탐색 시작
            if graph[cur][next] and indegree[next] == 0:
                queue.append(next)

    return " ".join(list(map(str, answer)))


def solution():
    cnt = 0

    while cnt < t:
        n, ranks, m, changes = getInput()
        graph, indegree = makeRanksToGraph(ranks=ranks, n=n)

        for c1, c2 in changes:
            if graph[c1][c2]:
                graph[c1][c2] = False
                graph[c2][c1] = True
                indegree[c2] -= 1
                indegree[c1] += 1
            else:
                graph[c2][c1] = False
                graph[c1][c2] = True

                indegree[c1] -= 1
                indegree[c2] += 1

        answer = getRank(graph=graph, indegree=indegree, n=n)

        print(answer)

        cnt += 1

    return


t = int(input())
solution()
