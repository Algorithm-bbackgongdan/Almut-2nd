# 표현 가능한 이진트리
def makeBinaryNumber(number):
    reverseBinaryNumber = []
    while number != 1:
        reverseBinaryNumber.append(str(number % 2))
        number //= 2
    reverseBinaryNumber.append("1")
    binaryNumber = ''.join(reverseBinaryNumber[::-1])
    binaryTreeSize = 1
    while binaryTreeSize < len(binaryNumber):
        binaryTreeSize = (binaryTreeSize + 1) * 2 - 1
    binaryNumber = "0" * (binaryTreeSize - len(binaryNumber)) + binaryNumber
    return binaryNumber

def checkPossible(start, end, binaryString):
    if start == end:
        return binaryString[start]
    mid = (start + end) // 2
    left = checkPossible(start, mid-1, binaryString)
    if not left or (binaryString[mid] == "0" and left == "1"): return False
    right = checkPossible(mid+1, end, binaryString)
    if not right or (binaryString[mid] == "0" and right == "1"): return False
    if left == "0" and right == "0" and binaryString[mid] == "0": return "0"
    return "1"

def solution(numbers):
    answer = []
    for number in numbers:
        binaryNumber = makeBinaryNumber(number)
        if checkPossible(0, len(binaryNumber)-1, binaryNumber):
            answer.append(1)
        else:
            answer.append(0)
    return answer

# print(solution([7, 42, 5]))
# print(solution([63, 111, 95]))