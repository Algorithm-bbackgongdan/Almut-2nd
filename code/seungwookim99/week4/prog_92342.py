# 양궁대회
from itertools import product


def calc_can_win(ap, lion):
    # 두 과녁이 주어졌을 때 우승 여부와 점수차 계산
    score_ap, score_lion = 0, 0
    for i in range(11):
        if ap[i] == 0 and lion[i] == 0:
            continue
        if ap[i] >= lion[i]:
            score_ap += 10 - i
        else:
            score_lion += 10 - i
    return (True, score_lion - score_ap) if score_lion > score_ap else (False, 0)


def calc(case, info, min_shots, n):
    lion = [0] * 11
    for i in range(11):
        if case[i] == False:
            continue
        if min_shots[i] <= n:
            lion[i] = min_shots[i]
            n -= min_shots[i]
    if n > 0:
        lion[-1] += n
    can_win, score = calc_can_win(info, lion)
    return (can_win, score, lion)


def sort_filtered(L):
    return sorted(
        L,
        key=lambda x: (
            -x[10],
            -x[9],
            -x[8],
            -x[7],
            -x[6],
            -x[5],
            -x[4],
            -x[3],
            -x[2],
            -x[1],
            -x[0],
        ),
    )


def solution(n, info):
    answer = []
    candidate = []
    min_shots = [0] * 11
    for i in range(11):
        min_shots[i] = info[i] + 1  # 10-i 점을 얻을 수 있는 최소 화살 수

    for case in product([True, False], repeat=11):
        # 해당 case에 대해 이길 수 있는 방법, 점수 계산
        win, score, lion = calc(case, info, min_shots, n)
        if not win:
            continue
        candidate.append((score, lion))

    if len(candidate) == 0:
        return [-1]
    candidate = sorted(candidate, key=lambda x: -x[0])  # 점수로 내림차순 정렬
    max_score = candidate[0][0]

    # 최대점수차로 이길 수 있는 방법들 filter
    filtered = []
    for elem in candidate:
        if elem[0] != max_score:
            break
        filtered.append(elem[1])
    return sort_filtered(filtered)[0]
