DAYS_PER_MONTH = 28
DAYS_PER_YEAR = 12 * 28


def calcDateDiff(prev, cur):
    prevYYYY, prevMM, prevDD = map(int, prev.split("."))
    curYYYY, curMM, curDD = map(int, cur.split("."))

    yearDiff = curYYYY - prevYYYY
    monthDiff = curMM - prevMM
    dayDiff = curDD - prevDD

    return yearDiff * DAYS_PER_YEAR + monthDiff * DAYS_PER_MONTH + dayDiff


def solution(today, termList, privacies):
    answer = []
    terms = dict()

    for termItem in termList:
        termType, termMonth = termItem.split(" ")
        terms[termType] = int(termMonth)

    for i in range(len(privacies)):
        privacy = privacies[i]
        validDate, termType = privacy.split(" ")
        dateDiff = calcDateDiff(validDate, today)

        if dateDiff >= terms[termType] * DAYS_PER_MONTH:
            answer.append(i + 1)

    return answer
