def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            # 부모는 방문했고, 자식노드(본인)는 방문 안 한 노드만 dfs
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[child] = 0

    visited[0] = 1
    dfs(1, 0)

    return max(answer)
