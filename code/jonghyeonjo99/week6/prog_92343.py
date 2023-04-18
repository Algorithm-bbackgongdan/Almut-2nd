# 실패코드
from collections import deque

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
visited = [0 for i in range(18)]
queue = []
deque_q = deque(queue)

def bfs(node):
  global sheep
  global wolf
  sheep = 0
  wolf = 0
  visited[node] = 1
  queue.append([node,info[node]])
  while queue:
    u = queue.pop(0)
    if info[u[1]] == 0:
      sheep += 1
    else:
      wolf += 1
    if sheep <= wolf:
      break
    for i in range(len(edges)):
      next_node = edges[i][1]
      if edges[i][0] == u[0] and visited[next_node] == 0:
        visited[next_node] = 1
        queue.append([next_node,info[next_node]])
    queue.sort(key=lambda x:(x[1],x[0]))


def solution(info, edges):
    bfs(0)
    answer = sheep
    return answer
    
#구글링 코드
def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0

	# 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)