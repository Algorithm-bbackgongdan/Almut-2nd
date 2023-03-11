import sys

read = sys.stdin.readline

# 예시 1 : 16
# cap = 4
# n = 5
# deliveries = [1, 0, 3, 1, 2]
# pickups = [0, 3, 0, 4, 0]

# 예시 2 : 30
cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]


def solution(cap, n, deliveries, pickups):
    i, j = n - 1, n - 1

    while i >= 0 and deliveries[i] == 0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1

    answer = 0

    while i >= 0 or j >= 0:
        answer += (max(i, j) + 1) * 2

        # 배달
        cur = cap
        while i >= 0 and cur:
            if deliveries[i] > cur:
                deliveries[i] -= cur
                cur = 0
            else:
                cur -= deliveries[i]
                deliveries[i] = 0
                while i >= 0 and deliveries[i] == 0:
                    i -= 1

        # 수거
        cur = cap
        while j >= 0 and cur:
            if pickups[j] > cur:
                pickups[j] -= cur
                cur = 0
            else:
                cur -= pickups[j]
                pickups[j] = 0
                while j >= 0 and pickups[j] == 0:
                    j -= 1

    return answer


print(solution(cap, n, deliveries, pickups))
