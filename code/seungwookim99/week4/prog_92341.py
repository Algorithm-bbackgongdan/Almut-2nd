# 주차 요금 계산
def parse_to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def get_times_sum(times):
    res = 0
    for i in range(0, len(times), 2):
        res += times[i + 1] - times[i]
    return res


def calc_fee(times, fees):
    times_sum = get_times_sum(times)
    res = fees[1]
    if times_sum <= fees[0]:
        return res
    res += ((times_sum - fees[0]) // fees[2]) * fees[3]
    # 나머지 0이 아니면 올림처리 (단위 요금 추가)
    if (times_sum - fees[0]) % fees[2] != 0:
        res += fees[3]
    return res


def solution(fees, records):
    answer = []
    cars = dict()
    # dictionary에 차량 번호를 key로 시간 value들 저장
    for record in records:
        data = record.split(" ")
        time = parse_to_minutes(data[0])
        num = data[1]
        if num in cars.keys():
            cars[num].append(time)
        else:
            cars[num] = [time]

    # 출차 내역 없는 차량 23:59 추가
    out_time = parse_to_minutes("23:59")
    for num in cars.keys():
        if len(cars[num]) % 2 == 1:
            cars[num].append(out_time)

    # 차량 번호 오름차순대로 요금 추가
    for num in sorted(cars.keys()):
        answer.append(calc_fee(cars[num], fees))
    return answer
