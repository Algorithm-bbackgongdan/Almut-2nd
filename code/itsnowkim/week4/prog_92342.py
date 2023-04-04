def solution(n, info):
	# 어피치의 총 점수 계산
    apeach = sum([10-i for i in range(10) if info[i]])
    # 과녁의 각 점수별 실질적으로 얻어지는 점수
    score = [(10-i)*2 if info[i] else 10-i for i in range(10)]
    # BFS를 위한 queue. 10점을 쏘지 않은 경우 기본 추가
    queue = [[0]]
    answer = []
    # 10점을 쏠 수 있는 경우, 쏜 경우를 queue에 추가
    if n >= info[0]+1:
        queue.append([info[0]+1])
        
    while queue:
        recent = queue.pop(0)
        # 주어진 화살을 다 쐈거나, 10~1점까지 다 쏜 경우
        if sum(recent) == n or len(recent) == 10:
            new = sum([score[i] for i in range(len(recent)) if recent[i]])
            old = sum([score[i] for i in range(len(answer)) if answer[i]])
            # apeach보다 많은 점수를, 그리고 기존 answer 이상의 점수를 얻었다면 update
            if new > apeach and new >= old:
                answer = recent
        # 아직 덜 쐈는데, 이번 점수에 (어피치+1)을 쏠 수 있다면
        elif sum(recent)+info[len(recent)]+1 <= n:
        	# 쏜 경우, 안 쏜 경우 모두 queue에 append
            queue.append(recent + [info[len(recent)]+1])
            queue.append(recent + [0])
        # 아직 덜 쐈는데, 쏠 화살이 안 남아있다면, 안 쏜 경우만 append
        else :
            queue.append(recent + [0])
    # apeach보다 많은 점수를 낼 수 없다면, [-1] return
    if not answer:
        return [-1]
    # 그렇지 않다면, [answer + 남은 점수 안쏘고 + 0점에 다 쏘기] return
    return answer + [0]*(10 - len(answer)) + [n-sum(answer)]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) #[0,2,2,0,1,0,0,0,0,0,0]
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0])) #[-1]
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1])) #[1,1,2,0,1,2,2,0,0,0,0]
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) #[1,1,1,1,1,1,1,1,0,0,2]