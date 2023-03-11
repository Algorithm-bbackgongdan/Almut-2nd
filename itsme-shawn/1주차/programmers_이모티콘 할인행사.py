import sys
from itertools import product

read = sys.stdin.readline

users = [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900],
]
emoticons = [1300, 1500, 1600, 4900]
# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]


def solution(users, emoticons):
    answer = [0, 0]
    discount_list = [10, 20, 30, 40]
    answer_temp = []

    for discounts in product(discount_list, repeat=len(emoticons)):
        after_emoticons = [0] * len(emoticons)
        # print("discounts", discounts)
        for i, discount in enumerate(discounts):
            after_emoticons[i] = int(emoticons[i] * (100 - discount) / 100)
        # print("after_emoticons", after_emoticons)

        user_purchase = [0] * len(users)
        user_purchase_temp = [0] * len(users)
        join = 0

        for i in range(len(users)):
            # user_purchase = [0] * len(users)
            # user_purchase_temp = [0] * len(users)
            # join = 0
            for j in range(len(emoticons)):
                # 일단 구매 의향
                if users[i][0] <= discounts[j]:
                    user_purchase_temp[i] += after_emoticons[j]

            if user_purchase_temp[i] >= users[i][1]:
                user_purchase_temp[i] = 0
                join += 1
            else:
                user_purchase[i] = user_purchase_temp[i]

        # print("user_purchase", user_purchase)
        # print("join", join)

        answer_temp.append([join, sum(user_purchase)])
    answer_temp.sort(key=lambda x: (-x[0], -x[1]))

    return answer_temp[0]


print(solution(users, emoticons))
