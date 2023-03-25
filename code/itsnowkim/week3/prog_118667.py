# 듀 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    answer = 0
    total1 = sum(queue1)
    total2 = sum(queue2)
    total = total1 + total2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 전체 합이 홀수면 불가능
    if total % 2 != 0:
        return -1
    
    # greedy하게 접근
    for _ in range(4*len(queue1)):
        if total1 > total2:
            total1 -= queue1[0]
            total2 += queue1[0]
            queue2.append(queue1.popleft())
        elif total1 < total2:
            total2 -= queue2[0]
            total1 += queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1

    return -1

    
# print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
# print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
# print(solution([1, 1],[1, 5]))


