from collections import deque


def solution(queue1, queue2):
    answer = 0

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 계속 옮기다 원래와 같게 되면 두 큐의 합을 같게 못 만든다.
    limit = 2 * (len(queue1) + len(queue2))

    d1 = deque(queue1)
    d2 = deque(queue2)

    # 애초에 같게 만들 수 없는 경우
    if (sum1 + sum2) % 2 == 1:
        return -1

    while True:
        if sum1 == sum2:
            break

        if len(d1) == 0 or len(d2) == 0 or answer >= limit:
            answer = -1
            break

        # 그리디하게 옮긴다.
        if sum1 > sum2:
            front = d1.popleft()
            d2.append(front)
            sum1 -= front
            sum2 += front
        else:
            front = d2.popleft()
            d1.append(front)

            sum2 -= front
            sum1 += front

        answer += 1

    return answer
