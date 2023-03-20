def get_break_date(privacy_date, private_type, term_dict):
    break_year, break_month, break_date = map(int, privacy_date.split("."))

    # 약관 유효기간의 월을 더함
    break_month += term_dict[private_type]

    # 년, 월 계산
    while break_month > 12:
        break_month -= 12
        break_year += 1

    break_year = str(break_year)
    break_month = str(break_month)
    break_date = str(break_date)

    if int(break_month) < 10:
        break_month = "0" + str(break_month)

    if int(break_date) < 10:
        break_date = "0" + str(break_date)

    return break_year + break_month + break_date  # YYYYMMDD


def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    for term in terms:
        term_type, term_duration = term.split()
        term_dict[term_type] = int(term_duration)

    for i, privacy in enumerate(privacies):
        privacy_date, privacy_type = privacy.split()

        # 개인정보의 파기날짜(break_date) 를 구함
        # 리턴값은 "YYYYMMDD" 형식
        break_date = get_break_date(privacy_date, privacy_type, term_dict)

        # 오늘 날짜를 "YYYYMMDD" 형식으로 맞춤
        today_date = today.replace(".", "")

        # print(break_date, today_date)

        # 파기날짜 <= 현재날짜 인 경우 파기
        if break_date <= today_date:
            answer.append(i + 1)

    # print(answer)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result : [1,3]

print(solution(today, terms, privacies))
