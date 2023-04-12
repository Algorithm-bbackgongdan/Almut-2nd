def solution(name):
    answer = 0
    minMove = len(name) - 1

    for i, alpha in enumerate(name):
        # 위, 아래 이동
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)

        # 연속된 A의 위치를 구함
        next = i + 1
        while next < len(name) and name[next] == 'A' : 
            next += 1

        # 처음 -> 연속된 A 왼쪽 -> 처음 -> 연속된 A 오른쪽
        moveForward = 2 * i + len(name) - next

        # 처음 -> 연속된 A 오른쪽 -> 처음 -> 연속된 A 왼쪽
        moveBackward = 2*(len(name) - next) + i

        # 지금까지 계산했던 minMove와 비교
        minMove = min(minMove, moveForward, moveBackward)
        

    return answer + minMove

