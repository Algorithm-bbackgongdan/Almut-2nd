# 수 묶기
# 수열의 합이 가장 크게 하라

N = int(input())
negative = []
positive = []

for _ in range(N):
    t = int(input())
    if t > 0:
        positive.append(t)
    else:
        negative.append(t)

# sort
positive.sort(reverse=True)
negative.sort()

# 결과 res에 저장
res = 0

for i in range(0, len(positive), 2):
    if i == len(positive)-1:
        res += positive[i]
        break

    temp1, temp2 = positive[i], positive[i+1]
    # 묶으려는 원소 중 1이 있다면 각자 더하는 것이 더 크다.
    if temp1 == 1 or temp2 == 1:
        res += (temp1 + temp2)
    else:
        res += (temp1 * temp2)

for i in range(0, len(negative), 2):
    if i == len(negative)-1:
        res += negative[i]
        break
    temp1, temp2 = negative[i], negative[i+1]
    # 묶으려는 원소 중 0이 있다면 묶어서 없애는 것이 더 크다.
    if temp1 == 0 or temp2 == 0:
        continue
    else:
        res += (negative[i] * negative[i+1])

print(res)