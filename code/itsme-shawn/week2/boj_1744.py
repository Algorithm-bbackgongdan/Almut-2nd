# 너무 중구난방식 풀이라서 맘에 들지는 않음,,,

import sys

read = sys.stdin.readline

n = int(read())
nums = sorted([int(read()) for _ in range(n)], reverse=True)

res = 0
positive_last_idx = n - 1  # 마지막 양수의 인덱스
is_all_negative = True
is_all_positive = True

for i in range(len(nums)):
    if nums[i] <= 0:
        is_all_positive = False
    else:
        is_all_negative = False
        positive_last_idx = i

if is_all_positive:
    positive_last_idx = n - 1
elif is_all_negative:
    positive_last_idx = 0  # 전부 음수인 경우는 positive_last_idx 를 0 으로 처리

# print("is_all_positive", is_all_positive)
# print("is_all_negative", is_all_negative)
# print("non_positive_first_idx", positive_last_idx)

# 양수인 부분 처리
# 1은 더해줘야함
for i in range(0, positive_last_idx, 2):
    temp = nums[i]
    if nums[i + 1] > 1:
        temp *= nums[i + 1]
    elif nums[i + 1] == 1:
        temp += nums[i + 1]
    res += temp

# 양수 하나 남았을 때 예외처리
# res 에 더해줌
if positive_last_idx % 2 == 0:
    last_positive_num = nums[positive_last_idx]
    if last_positive_num > 0:
        res += last_positive_num


# 양수 아닌 부분 처리
for j in range(n - 1, positive_last_idx - 1, -2):
    if nums[j] <= 0:
        temp = nums[j]
        if (
            j - 1 >= 0 and nums[j - 1] <= 0
        ):  # 전부 음수인 경우 j - 1 이 -1 이 될 수 있어서 j-1>=0 인지 검사
            temp *= nums[j - 1]
        res += temp


print(res)
