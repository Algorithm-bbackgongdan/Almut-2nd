from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1) + len(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    if ((sum_q1 + sum_q2) % 2 == 1):
        return -1
    while (1):
        if(answer >= 2*n):
            return -1
            break
        if(sum_q1 == sum_q2):
            break
        if(sum_q1 > sum_q2):
            temp1 = q1.popleft()
            q2.append(temp1)
            answer += 1
            sum_q1 -= temp1
            sum_q2 += temp1
        if(sum_q1 < sum_q2):
            temp2 = q2.popleft()
            q1.append(temp2)
            answer += 1
            sum_q1 += temp2
            sum_q2 -= temp2
    return answer