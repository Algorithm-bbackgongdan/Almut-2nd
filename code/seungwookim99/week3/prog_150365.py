import sys
sys.setrecursionlimit(10000)

dx = {
    'd': 1,
    'l': 0,
    'r': 0,
    'u': -1
}

dy = {
    'd': 0,
    'l': -1,
    'r': 1,
    'u': 0
}
def manhattan_distance(p1,p2):
    (x1,y1), (x2,y2) = p1, p2
    return abs(x1-x2) + abs(y1-y2)

def is_impossible(p1,p2,k):
    man_d = manhattan_distance(p1,p2)
    if man_d > k: # 최단경로보다 k가 작을 때
        return True
    return man_d % 2 != k % 2 # 홀수 / 짝수 번에 갈 수 있는지 여부

def solution(n, m, x, y, r, c, k):
    global answer
    global end
    global K
    K = k
    answer = ""
    start, end = (x,y), (r,c)
    if is_impossible(start, end, k):
        return "impossible"
    
    def inside_boundary(x,y):
        return (1 <= x <= n) and (1 <= y <= m)
    
    def dfs(x,y,moves):
        global answer
        if len(moves) == K:
            if (x == end[0]) and (y == end[1]):
                answer = moves # 정답 저장 및 dfs 종료
                return True
            else:
                return False
        steps_to_go = K - len(moves) # 남은 step
        shortest_path_len = manhattan_distance((x,y),end) # 현위치 기준 최단거리
        if steps_to_go < shortest_path_len:
            return False
        
        for direction in ['d','l','r','u']:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if inside_boundary(nx,ny):
                solved = dfs(nx,ny,moves+direction)
                if solved:
                    return True
        return False
    dfs(x,y,"")
    return answer