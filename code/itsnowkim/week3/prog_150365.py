# 미로 탈출 명령어
def check_possible(optimal_movement, k):
    if k < optimal_movement:
        return False
    
    if (k % 2) != (optimal_movement % 2):
        return False
    
    return True

def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    # impossible 여부 판단
    optimal = abs(x- r) + abs(y -c)
    if not check_possible(optimal, k):
        return answer
    
    # 방향 우선순위에 따라 dfs recursive하게 호출
    stack = [(x, y, [])]
    while stack:
        x_pos, y_pos, path = stack.pop()
        if len(path) == k and (x_pos, y_pos) == (r,c):
            answer = ''.join(path)
            break
        # impossible 여부 판단
        optimal = abs(x_pos- r) + abs(y_pos -c)
        remain = k-len(path)
        if not check_possible(optimal,remain):
            continue

        if x_pos > 1:
            stack.append((x_pos-1, y_pos, path + ['u']))
        if y_pos < m:
            stack.append((x_pos, y_pos+1, path+['r']))
        if y_pos > 1:
            stack.append((x_pos, y_pos-1, path + ['l']))
        if x_pos < n:
            stack.append((x_pos+1, y_pos, path+['d']))

    return answer
    

# print(solution(3, 4, 2, 3, 3, 1, 5)) # dllrl
# print(solution(2, 2, 1, 1, 2, 2, 2)) # dr
# print(solution(3, 3, 1, 2, 3, 3, 4)) # impossible