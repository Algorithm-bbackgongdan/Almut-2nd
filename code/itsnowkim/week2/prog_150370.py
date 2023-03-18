# 개인정보 수집 유효기간
def solution(today, terms, privacies):
    answer = []

    def date2day(date):
        year, month, day = map(int, date.split("."))
        return (year * 12 * 28) + (month * 28) + day
    
    # today
    today = date2day(today)
    
    # terms
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28
    
    # privacies
    for idx, priv in enumerate(privacies):
        date, term = priv.split()
        if date2day(date) + termsInfo[term] <= today:
            answer.append(idx+1)
        
    return answer

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))