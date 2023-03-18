# 1. 십진수 -> 이진수 변환
def decimalToBinary(number):
    binary = ""

    while number != 0:
        remain = number % 2
        number = number // 2

        binary = str(remain) + binary

    return binary


# 2. 이진수의 자릿수 를 (2^n - 1) 로  확장 ( 포화이진트리노드 개수인 2^n -1 )
def getExpandBinary(binary):
    # ex. 101010 (6자리) => 0101010 (7자리) 로 확장해야함
    # 자리수 확장 체크
    n = 1
    while len(binary) > 2**n - 1:
        n += 1

    # (2^n - 1) 자릿수로 변환
    expand_count = 2**n - 1 - len(binary)

    return "0" * expand_count + binary


# 3. 포화이진트리로 만들 수 있는 이진수인지 체크하는 함수
def check(binary):
    bin_num = binary

    if len(bin_num) == 1:
        return True

    half = len(bin_num) // 2

    # 가운데 수가 1 이면 왼쪽그룹 과 오른쪽그룹 재귀적으로 검사
    if bin_num[half] == "1":
        left_check = check(bin_num[:half])  # 왼쪽그룹 check
        right_check = check(bin_num[half + 1 :])  # 오른쪽그룹 check

    # 가운데 수가 0 이면 왼쪽그룹 과 오른쪽그룹도 0 이여야 한다. ( 1 이 있으면 안 됨)
    else:  # if bin_num[half] == 0:
        if "1" in bin_num[:half] or "1" in bin_num[half + 1 :]:
            return False
        else:
            return True

    # 왼쯕그룹과 오른쪽그룹 검사 결과가 둘 다 True 이면 최종 True
    if left_check and right_check:
        return True
    else:
        return False


def solution(numbers):
    answer = []

    for number in numbers:
        binary = decimalToBinary(number)  # 1
        expandBinary = getExpandBinary(binary)  # 2
        ans = int(check(expandBinary))  # 3
        answer.append(ans)

    return answer


numbers = [7, 42, 5]
# numbers = [63, 111, 95]

print(solution(numbers))
