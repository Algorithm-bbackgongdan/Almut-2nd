def parseDateToDays(date):
    date_split = date.split('.')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])

    return day + 28 * month + 12 * 28 * year

def makeTermsDictionary(terms):
    res = {}
    for term in terms:
        type_ = term.split(' ')[0]
        month = int(term.split(' ')[1])
        res[type_] = month        
    return res


def solution(today, terms, privacies):
    answer = []
    parsedToday = parseDateToDays(today)
    termsDict = makeTermsDictionary(terms)
    for i, privacy in enumerate(privacies):
        date = privacy.split(' ')[0]
        parsedDate = parseDateToDays(date)
        type_ = privacy.split(' ')[1]
        expiration = termsDict[type_]
        
        if (parsedDate + 28 * expiration) <= parsedToday:
            answer.append(i+1)
    
    return answer