from itertools import combinations_with_replacement as cr

def solution(n, info):
    # 중복조합으로 모든 경우 탐색하면서 정답 갱신
    # 최대로 점수 차이가 클 때의 점수 분포 + 그 때의 점수 차이 값(max[-1])
    max = [-1] * 12
    for comb in cr(range(11), n):
        cur = [0] * 12
        # 점수별 화살 개수
        for c in comb:
            cur[10 - c] += 1
        
        # 점수 차이 계산
        for i in range(11):
            # 라이언 점수 획득
            if cur[i] > info[i]:
                cur[-1] += 10 - i
            # 어피치 점수 획득
            elif info[i] != 0:
                cur[-1] -= 10 - i
        
        # 라이언이 우승하지 못하는 경우
        if cur[-1] <= 0:
            continue
            
        # 기존의 점수 차이 최댓값을 갱신하는 경우
        if cur[::-1] > max[::-1]:
            max = cur

    return [-1] if max[-1] <= 0 else max[:-1]