import sys
from collections import deque

input = sys.stdin.readline
X = 0
ALL_ZERO = -1

# inputs
n, m, t = map(int, input().split())
B = [deque(list(map(int, input().split()))) for _ in range(n)]
B = [[]] + B  # dummy 추가

tasks = [list(map(int, input().split())) for _ in range(t)]


def rotate(x, d, k):
    shift_num = k % m if k != 1 else 1
    if d == 1:
        shift_num = (m - shift_num) % m
    for i in range(x, n + 1, x):
        for _ in range(shift_num):
            elem = B[i].pop()
            B[i].appendleft(elem)
    return


def average():
    total = 0
    cnt = 0
    for i in range(1, n + 1):
        for j in range(m):
            if B[i][j] == X:
                continue
            total += B[i][j]
            cnt += 1
    if cnt == 0:
        return ALL_ZERO
    return total / cnt


def check_adjacent():
    candidate = set()
    for i in range(1, n + 1):
        curr, next = 0, 1
        for _ in range(m):
            if B[i][curr] == B[i][next] and B[i][curr] != X:
                candidate.add((i, curr))
                candidate.add((i, next))
            curr = next
            next += 1
            if next == m:
                next = 0

    # colwise
    for j in range(m):
        curr, next = 1, 2
        for _ in range(1, n):
            if B[curr][j] == B[next][j] and B[curr][j] != X:
                candidate.add((curr, j))
                candidate.add((next, j))
            curr = next
            next += 1

    candidate = list(candidate)
    for y, x in candidate:
        B[y][x] = X

    return len(candidate) > 0


is_all_zero = False
for x, d, k in tasks:
    rotate(x, d, k)
    is_deleted = check_adjacent()
    if not is_deleted:
        avg = average()
        if avg == ALL_ZERO:
            is_all_zero = True
            break
        for i in range(1, n + 1):
            for j in range(m):
                if B[i][j] == X:
                    continue
                if B[i][j] > avg:
                    B[i][j] -= 1
                elif B[i][j] < avg:
                    B[i][j] += 1

answer = 0
if not is_all_zero:
    for i in range(1, n + 1):
        answer += sum(B[i])
print(answer)
