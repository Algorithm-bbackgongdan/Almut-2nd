# 이모티콘 할인행사
# 가입 유저 최대로
# 이모티콘 판매 이익 최대
from itertools import product

def solution(users, emoticons):
    register_user_count = 0
    max_price = 0

    # 가능한 할인률은 10, 20, 30, 40.
    discounts = product([10, 20, 30, 40], repeat=len(emoticons))
    
    # user가 23 일 경우 30, 40부터 사니까, 사게 되는 할인률로 맞춰주는 것 먼저 시작
    for user in users:
        if user[0] <= 10:
            user[0] = 10
        elif 10 < user[0] <= 20:
            user[0] = 20
        elif 20 < user[0] <= 30:
            user[0] = 30
        elif 30 < user[0] <= 40:
            user[0] = 40
        # 이외에는 안사요~
    
    # 가능한 모든 할인률로 이모티콘의 판매 가격 결정
    for discount in discounts:
        user_count = 0
        sum_price = 0

        for user in users:
            paid = 0

            for i in range(len(emoticons)):
                # 조건에 만족하면 구매
                if (discount[i] >= user[0]):
                    rate = (100 - discount[i])
                    price100 = emoticons[i] * rate
                    paid += price100 // 100
            if paid >= user[1]:
                # 이모티콘 플러스로 옮겨감
                user_count += 1
            else:
                sum_price += paid

        if register_user_count < user_count:
            register_user_count = user_count
            max_price = sum_price
        elif register_user_count == user_count and max_price < sum_price:
            max_price = sum_price

    return [register_user_count, max_price]

print(solution([[40, 10000], [25, 10000]],[7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))