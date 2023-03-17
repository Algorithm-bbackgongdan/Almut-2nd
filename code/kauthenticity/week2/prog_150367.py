import math


# 포화 이진 트리로 만듦
def convertToFullBinaryTree(binary):
    treeHeight = int(math.log2(len(binary)))
    fullNodes = 2 ** (treeHeight + 1) - 1

    i = len(binary)
    while i < fullNodes:
        binary = "0" + binary
        i += 1

    return binary


# bit string으로 변환
def convertToBinaryString(number):
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

    binary = convertToFullBinaryTree(binary)

    return binary


# 표현 가능한 이진트리인지 확인
def isDescribable(binary):
    if len(binary) == 1:
        return True

    mid = len(binary) // 2

    leftSubtree = binary[:mid]
    parent = binary[mid]
    rightSubtree = binary[mid + 1 :]

    if parent == "0":
        # 더미 노드 아래에 기존 노드가 있을 수 없음
        if leftSubtree.count("1") > 0 or rightSubtree.count("1") > 0:
            return False
        # 아예 더미노드로만 서브트리 구성은 가능
        else:
            return True
    else:
        return isDescribable(leftSubtree) and isDescribable(rightSubtree)


def solution(numbers):
    answer = []

    for number in numbers:
        binary = convertToBinaryString(number)

        if isDescribable(binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer
