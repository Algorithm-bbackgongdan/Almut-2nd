from collections import defaultdict
from math import ceil


def solution(fees, records):
    answer = []
    infoDict = defaultdict(list)
    defaultTime, defaultFee, unitTime, unitFee = fees

    for record in records:
        time, carNumber, status = record.split(" ")
        infoDict[carNumber].append((time, status))

    infoList = sorted(infoDict.items())

    for carNumber, info in infoList:
        feeSum = 0
        parkTimeSum = 0

        # 출차 정보가 없는 경우
        if len(info) % 2 == 1:
            info.append(("23:59", "OUT"))

        for i in range(0, len(info), 2):
            inTime, _ = info[i]
            outTime, _ = info[i + 1]

            inHH, inMM = map(int, inTime.split(":"))
            outHH, outMM = map(int, outTime.split(":"))

            parkTime = (outHH * 60 + outMM) - (inHH * 60 + inMM)
            parkTimeSum += parkTime

        # 기본 요금 부과
        feeSum += defaultFee

        # 추가 요금 부과
        if parkTimeSum > defaultTime:
            extraTime = parkTimeSum - defaultTime
            feeSum += ceil(extraTime / unitTime) * unitFee

        answer.append(feeSum)

    return answer


# 기본 시간, 기본 요금, 단위 시간, 단위 요금
fees = [180, 5000, 10, 600]
# records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

print(solution(fees=fees, records=records))
