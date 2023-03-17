import sys

n = int(input())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]


def categorizeNumbers(nums):
    negatives = []
    isZero = False
    positives = []

    for num in nums:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            isZero = True

    # 양수는 내림차순으로 정렬
    positives.reverse()

    return negatives, isZero, positives


def bundleNumbers(nums):
    sum = 0
    remainedNumber = 0
    i = 0

    # 숫자를 두 개씩 묶음
    # 곱한기, 더하기 중 더 큰 방법으로 묶음
    while i + 1 < len(nums):
        multiply = nums[i] * nums[i + 1]
        add = nums[i] + nums[i + 1]

        if multiply > add:
            sum += multiply
        else:
            sum += add

        i += 2

    # 묶지 못하고 남은 숫자
    if i == len(nums) - 1:
        remainedNumber = nums[i]

    return sum, remainedNumber


def solution():
    nums.sort()

    negatives, isZero, positives = categorizeNumbers(nums)
    sum = 0

    negativeSum, negativeRemain = bundleNumbers(negatives)
    positiveSum, positiveRemain = bundleNumbers(positives)

    # 묶은 숫자들은 전부 더해 줌
    sum += negativeSum
    sum += positiveSum

    # 양수 중에 묶지 못한 숫자가 있으면 더해 줌
    sum += positiveRemain

    # 0이 포함돼 있지 않은데, 음수가 남은 경우
    # 0과 곱할 수 없으므로 음수를 더해줌
    if not isZero:
        sum += negativeRemain

    return sum


print(solution())
