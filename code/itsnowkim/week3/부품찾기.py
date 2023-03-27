import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
M = int(input())
target_list = list(map(int, sys.stdin.readline().split()))

# 배열의 개수가 1000000 개까지이므로 O(logN)의 알고리즘 필요
def find_item(target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return find_item(target, mid + 1, end)
    else:
        return find_item(target, start, mid -1)

# 정렬
array.sort()

# 있으면 yes, 없으면 no
for item in target_list:
    start = 0
    end = N-1
    answer = find_item(item, start, end)
    if answer != None:
        print('yes')
    else:
        print('no')

"""
5
8 3 7 9 2
3
5 7 9
"""