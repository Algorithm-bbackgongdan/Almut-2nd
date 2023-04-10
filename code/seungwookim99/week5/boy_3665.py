import sys
from collections import deque

input = sys.stdin.readline


def make_order(indegree, team, n, graph):
    for i in range(n):
        for j in range(i + 1, n):
            indegree[team[j]] += 1
            graph[team[i]].append(team[j])


def topology_sort(indegree, graph, n):
    q = deque()
    result = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cnt = 0
    while q:
        cnt += 1
        curr = q.popleft()
        result.append(curr)
        zero_indegree_exist = False
        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                if zero_indegree_exist:
                    return "?"
                q.append(i)
                zero_indegree_exist = True

    if cnt != n:
        return "IMPOSSIBLE"
    return " ".join(str(i) for i in result)


T = int(input())
answers = []
for _ in range(T):
    n = int(input())
    indegree = [0] * (n + 1)
    team = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    make_order(indegree, team, n, graph)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
        else:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1

    answers.append(topology_sort(indegree, graph, n))

for ans in answers:
    print(ans)
