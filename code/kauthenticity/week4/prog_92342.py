INFO_LAST_INDEX = 10


def calcScore(apeachInfo, ryanInfo):
    apeachScore = 0
    ryanScore = 0

    for i in range(0, 11):
        # 둘 다 몾 맞추면 점수를 얻지 못함
        if apeachInfo[i] == ryanInfo[i] == 0:
            continue

        if apeachInfo[i] >= ryanInfo[i]:
            apeachScore += 10 - i
        else:
            ryanScore += 10 - i

    return apeachScore, ryanScore


def isBetter(prevInfo, curInfo):
    for i in range(10, -1, -1):
        # 기존 정답보다 낮은 점수의 개수가 더 많음
        if prevInfo[i] < curInfo[i]:
            return True
        # 기존 정답보다 낮은 점수의 개수가 더 적으면, 조건 위배
        elif prevInfo[i] > curInfo[i]:
            return False

    # 비기는 경우는 이길 수 없음
    return False


def solution(n, info):
    answer = [-1]
    stack = []
    arrows = n
    index = 0
    ryanInfo = [0] * 11
    maxDiff = 0

    if arrows > info[index]:
        ryanShoot = info[index] + 1
        newInfo = ryanInfo[:]
        newInfo[index] = ryanShoot
        stack.append((index + 1, arrows - ryanShoot, newInfo))

    stack.append((index + 1, arrows, ryanInfo[:]))

    while stack:
        # 현재 쏠 과녁 index, 남은 화살 개수, 라이언 점수표
        index, arrows, ryanInfo = stack.pop()

        # 10점 -> 0점 다 돎
        if index > INFO_LAST_INDEX:
            # 주어진 화살을 다 쏘지 않은 경우
            if arrows > 0:
                ryanInfo[INFO_LAST_INDEX] = arrows

            apeachScore, ryanScore = calcScore(apeachInfo=info, ryanInfo=ryanInfo)
            curDiff = ryanScore - apeachScore

            if curDiff > maxDiff:
                answer = ryanInfo[:]
                maxDiff = curDiff

            # 점수 차이가 같은 경우에는 낮은 점수를 많이 맞힌 경우가 정답
            elif (
                curDiff > 0
                and curDiff == maxDiff
                and isBetter(prevInfo=answer, curInfo=ryanInfo)
            ):
                answer = ryanInfo[:]
                maxDiff = curDiff

            continue

        # 점수를 얻는 경우
        if arrows > info[index]:
            ryanShoot = info[index] + 1
            ryanInfo[index] = ryanShoot
            stack.append((index + 1, arrows - ryanShoot, ryanInfo[:]))

        # 점수를 얻지 않는 경우
        ryanInfo[index] = 0
        stack.append((index + 1, arrows, ryanInfo[:]))

    return answer


n = 5

# k점에 대해 맞힌 화살 수가 똑같으면 어피치가 점수를 가져감
# info[i]: 어피치가 10-i점을 맞힌 화살 개수

# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

print(solution(n, info))
