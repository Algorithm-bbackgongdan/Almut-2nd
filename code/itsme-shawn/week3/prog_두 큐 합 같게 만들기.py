from collections import deque


def solution(queue1, queue2):
    answer = -1
    cnt = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    limit_cnt = (len(q1) + len(q2)) * 2

    tot1 = sum(q1)
    tot2 = sum(q2)
    total = tot1 + tot2

    if total % 2 == 1:
        return -1
    else:
        target = total // 2
        while cnt <= limit_cnt:
            if tot1 < target:
                tmp = q2.popleft()
                q1.append(tmp)
                tot1 += tmp
                tot2 -= tmp
                cnt += 1
            elif tot1 > target:
                tmp = q1.popleft()
                q2.append(tmp)
                tot1 -= tmp
                tot2 += tmp
                cnt += 1
            elif tot1 == target:
                answer = cnt
                break

    return answer
