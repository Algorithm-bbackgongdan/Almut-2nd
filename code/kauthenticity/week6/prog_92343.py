from collections import defaultdict


def dfs(sheep, wolf, nextNodes, info):
    global answer
    answer = max(answer, sheep)

    for nextNode in nextNodes : 
        tempNextNodes = [tempNextNode for tempNextNode in nextNodes if tempNextNode != nextNode] # 다음 노드에서 현재 노드 제거
        tempNextNodes.extend(graph[nextNode]) # 현재 노드의 자식 노드 추가

        isWolf = info[nextNode]
        if isWolf + wolf >= sheep : 
            continue
        
        if isWolf : 
            dfs(sheep, wolf+1, tempNextNodes, info)
        else : 
            dfs(sheep+1, wolf, tempNextNodes, info)
        


def solution(info, edges):
    global answer, graph

    answer = 0
    graph = defaultdict(list)
    
    # make graph
    for v1, v2 in edges : 
        graph[v1].append(v2)

    dfs(1, 0, graph[0], info)
    
    return answer




info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info=info, edges=edges))
