# 주차 요금 계산


def get_parkingtime(in_time, out_time):
    in_time_to_minute = int(in_time[0:2]) * 60 + int(in_time[3:])
    out_time_to_minute = int(out_time[0:2]) * 60 + int(out_time[3:])

    return out_time_to_minute - in_time_to_minute


def get_totalfee(total_minute, fees):
    basic_time, basic_price, new_time, new_price = fees
    if total_minute <= basic_time:
        return basic_price
    else:
        if (total_minute - basic_time) % new_time == 0:
            add_price = int((total_minute - basic_time) / new_time) * new_price
        else:
            add_price = int((total_minute - basic_time) / new_time + 1) * new_price
        return basic_price + add_price


def solution(fees, records):
    answer = []

    dic = dict()  # 누적계산용
    lst = []

    for record in records:
        time, car_num, detail = record.split()

        # IN
        if detail == "IN":
            if car_num in dic:
                dic[car_num][0] = time

            else:
                dic[car_num] = [time, 0]  # (들어온 시간, 누적 주차시간)

        # OUT
        elif detail == "OUT":
            dic[car_num][1] += get_parkingtime(dic[car_num][0], time)
            dic[car_num][0] = False

    # 요금 계산하면서 출차 안 한 차도 같이 처리
    for car_num in dic:
        if dic[car_num][0]:
            dic[car_num][1] += get_parkingtime(dic[car_num][0], "23:59")
            dic[car_num][0] = False

    lst = sorted(dic.items())
    print(lst)

    for l in lst:
        answer.append(get_totalfee(l[1][1], fees))

    print(answer)

    return answer
