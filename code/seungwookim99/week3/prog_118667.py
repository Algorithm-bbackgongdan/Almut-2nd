from collections import deque

def solution(queue1, queue2):
    MAX_ITERATION = 2*(len(queue1) + len(queue2))
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = q1_sum_orig, q2_sum_orig = sum(q1), sum(q2)
    if (q1_sum + q2_sum) % 2 == 1:
        return -1
    while q1 and q2 and (answer < MAX_ITERATION):
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            elem = q1.popleft()
            q2.append(elem)
            q1_sum -= elem
            q2_sum += elem
        elif q1_sum < q2_sum:
            elem = q2.popleft()
            q1.append(elem)
            q2_sum -= elem
            q1_sum += elem
        answer += 1
        
    if len(q1) == 0 or len(q2) == 0 or answer == MAX_ITERATION:
        answer = -1
    return answer