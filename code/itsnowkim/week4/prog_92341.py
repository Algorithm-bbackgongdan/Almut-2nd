from math import ceil

def calculate_fee(fees, duration):
    dur = sum(duration)
    
    # 기본요금만 지불
    answer = fees[1]
    if dur > fees[0]:
        answer += ceil((dur-fees[0])/fees[2]) * fees[3]

    return answer

def calculate_dur(in_time, out_time):
    if len(in_time) > len(out_time):
        out_time.append('23:59')
    
    # 머무른 시간 계산
    res = []
    for t1, t2 in zip(in_time, out_time):
        h, m = t1.split(':')
        total1 = int(h) * 60 + int(m)
        h, m = t2.split(':')
        total2 = int(h) * 60 + int(m)

        res.append(total2 - total1)
    
    return res

def solution(fees, records):
    answer = []
    in_car = {}
    out_car = {}
    for rec in records:
        time, number, option = rec.split(' ')
        if option == 'IN':
            if number not in in_car:
                in_car[number] = [time]
            else:
                in_car[number].append(time)
        else:
            if number not in out_car:
                out_car[number] = [time]
            else:
                out_car[number].append(time)
    
    in_car = dict(sorted(in_car.items()))
    
    for key, in_time in in_car.items():
        # 출차 있는지 확인
        if key in out_car:
            # 머무른 시간 계산
            duration = calculate_dur(in_time, out_car[key])
        else:
            duration = calculate_dur(in_time, ["23:59"])
        
        fee = calculate_fee(fees, duration)
        answer.append(fee)

    return answer


#[14600, 34400, 5000]
# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
#[0, 591]
# print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
#[14841]
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))