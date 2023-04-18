# 조이스틱
def calculation(alphabet):
    temp = min(ord(alphabet) - ord('A'), ord('Z') - ord(alphabet) + 1)
    return temp

def solution(name):
    # 조이스틱 조작 횟수
    answer = 0
    # 한 방향으로만 이동했을 때 좌우 최소 이동 횟수
    moves = len(name) - 1
    
    for idx, alpha in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += calculation(alpha)
    
        # 해당 알파벳 이후 연속된 A 문자열의 끝 인덱스 찾기
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
    
        """
        idx 기준 방향 전환하는 두 가지 경우의 수 중 최소값으로 갱신
        """
        # 오른쪽으로 진행중이었을 경우
        left_backward = idx*2 + (len(name) - next)
        # 왼쪽으로 진행중이었을 경우
        right_backward = idx + (len(name)-next)*2
        
        moves = min([moves, left_backward, right_backward])
    
    # 좌,우 이동의 최소값을 더해 줌.
    answer += moves
    return answer