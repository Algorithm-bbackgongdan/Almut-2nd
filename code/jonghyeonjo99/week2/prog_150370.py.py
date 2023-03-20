def solution(today, terms, privacies):
    answer = []
    dict = {}
    cnt = 0
    
    today_spilt = today.split(".")
    year = int(today_spilt[0])
    month = int(today_spilt[1])
    day = int(today_spilt[2])
    totalDay = year*12*28 + month*28 + day
    
    for i in terms:
        type,month = i.split(" ")
        dict[type] = month
    
    for j in privacies:
        privacies_spilt = j.split(" ")
        privacies_date = privacies_spilt[0]
        privacies_type = privacies_spilt[1]
        privacies_date_spilt = privacies_date.split(".")
        p_year = int(privacies_date_spilt[0])
        p_month = int(privacies_date_spilt[1])
        p_day = int(privacies_date_spilt[2])
        p_totalDay = p_year*12*28 + p_month*28 + p_day + int(dict[privacies_type]) * 28
        cnt += 1
        if totalDay >= p_totalDay:
            answer.append(cnt)
    return answer