from collections import deque

def solution(info, edges):
    answer = 0

    # graph 만들기
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)

    # root 노드부터 탐색 - bfs로 탐색해서, 결과 업데이트
    q = deque([(0, [], 0, 0)]) # 방문노드, 앞으로 갈 수 있는 노드의 리스트, 양, 늑대

    while q:
        curr, possible, sheep, wolf = q.popleft()
        # 양과 늑대 업데이트
        if info[curr] == 0:
            sheep+=1
        else:
            wolf+=1

        # answer update
        answer = max(answer, sheep)

        # 종료 조건이면 종료
        if sheep<=wolf:
            continue

        # 현재 노드에서 앞으로 갈 수 있는 노드 업데이트
        for v in graph[curr]:
            possible.append(v)

        # possible에 있는 모든 노드를 q에 추가
        for idx, p in enumerate(possible):
            temp = possible[0:idx]+possible[idx+1:]
            q.append((p, temp, sheep, wolf ))

    
    return answer

# root 노드를 시작점으로, 탐색할 수 있는 모든 경로의 경우의 수를 만들어야 한다.
# print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])) #5
# print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])) #5