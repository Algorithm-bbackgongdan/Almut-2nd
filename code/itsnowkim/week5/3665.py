# 최종 순위
from collections import deque

# solution 함수
def solution():
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(n+1)]

    # 작년 순위대로 그래프 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[arr[i]].append(arr[j])
            indegree[arr[j]] += 1
    # print(graph)
    # print(indegree)
    # 올해 순위대로 graph, indegree 수정
    for item in changed:
        # 두 vertex의 그래프 수정
        a, b = item
        # 작년에 앞선 팀은 어디인가?
        if arr.index(a) < arr.index(b):
            # 그래프 추가, 위상 감소
            graph[b].append(a)
            indegree[b] -= 1
            # 그래프 제거, 위상 증가
            graph[a].remove(b)
            indegree[a] += 1
        else:
            # 그래프 추가, 위상 감소
            graph[a].append(b)
            indegree[a] -= 1
            # 그래프 제거, 위상 증가
            graph[b].remove(a)
            indegree[b] += 1

    # queue 순회하면서 순서 출력
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    if not q:
        print("IMPOSSIBLE")
        return
    
    result = True
    answer = []
    while q:
        if len(q)>1:
            result = False
            break

        temp = q.popleft()
        answer.append(temp)
        for j in graph[temp]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
            elif indegree[j] < 0:
                result = False
                break
    if not result or len(answer)<n:
        print("IMPOSSIBLE")
    else:
        print(*answer)
    return
K = int(input())
# test case만큼 코드 실행
for _ in range(K):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    changed = [tuple(map(int,input().split())) for _ in range(m)]

    solution()