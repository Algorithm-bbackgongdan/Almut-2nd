def decimalToBinaryString(number):
    binary = ''
    while number > 0:
        if number % 2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        number //= 2
    treeLevel = 1
    while 2**treeLevel - 1 < len(binary):
        treeLevel += 1
    binary = '0' * ((2**treeLevel - 1) - len(binary)) + binary
    return binary

def isBinaryTree(S):
    if len(S) == 1:
        return True
    left = S[:len(S) // 2]
    mid = S[len(S)//2]
    right = S[len(S)//2 + 1:]
    if mid == '1':
        return isBinaryTree(left) and isBinaryTree(right)
    else:
        if ('1' in left) or ('1' in right):
            return False
        return True

def solution(numbers):
    answer = []
    for number in numbers:
        binary = decimalToBinaryString(number)
        if isBinaryTree(binary):
            answer.append(1)
        else:
            answer.append(0)
    return answer