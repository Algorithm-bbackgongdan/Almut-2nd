import sys

n, m = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))


def solution(n, m, lectures):
    low = max(lectures)
    high = sum(lectures)

    while low < high:
        mid = (low + high) // 2

        i = 0
        bluerayNum = 0
        lectureSum = 0

        while i < len(lectures):
            lecture = lectures[i]

            if lectureSum + lecture > mid:
                lectureSum = 0
                bluerayNum += 1

            lectureSum += lecture

            i += 1

        # 마지막에 못 더한 강의
        if lectureSum > 0:
            bluerayNum += 1

        # 블루레이 개수를 늘리기 위해선 강의의 길이를 줄여야 한다.
        if bluerayNum <= m:
            high = mid
        # 블루레이 개수를 줄이기 위해선 강의의 길이르 늘려려야 한다.
        else:
            low = mid + 1

    return low


print(solution(n, m, lectures))
