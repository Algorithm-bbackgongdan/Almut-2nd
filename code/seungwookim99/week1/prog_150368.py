from itertools import product
DISCOUNT_RATE = [10,20,30,40]

def purchaseCost(wishRatio, emoticons, discountRatios):
    cost = 0
    for i in range(len(emoticons)):
        if discountRatios[i] >= wishRatio:
            cost += emoticons[i] * (100 - discountRatios[i]) // 100
    return cost

def solution(users, emoticons):
    candidate = []
    for discountRatios in product(DISCOUNT_RATE, repeat=len(emoticons)):
        plusMember = 0
        salesPriceSum = 0
        for (wishRatio, criteriaPrice) in users:
            costExpected = purchaseCost(wishRatio, emoticons, discountRatios)
            if costExpected >= criteriaPrice:
                plusMember += 1
            else:
                salesPriceSum += costExpected
        candidate.append((plusMember, salesPriceSum))
    candidate.sort(key = lambda x : (-x[0], -x[1]))
    return candidate[0]