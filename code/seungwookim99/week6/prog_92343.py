def solution(info, edges):
    global answer
    answer = 0
    visited = [False] * len(info)
    visited[0] = True

    def dfs(sheep, wolf):
        global answer
        answer = max(sheep, answer)
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b] = True
                if info[b] == 1 and sheep > wolf + 1:
                    dfs(sheep, wolf + 1)
                elif info[b] == 0:
                    dfs(sheep + 1, wolf)
                visited[b] = False
        return

    dfs(1, 0)
    return answer
