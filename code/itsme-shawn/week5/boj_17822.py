import sys
from collections import defaultdict, deque

read = sys.stdin.readline


def is_exist_num(circles):
    for value in circles.values():
        for num_lst in value:
            if num_lst[1]:
                return True
    return False


n, m, t = map(int, read().split())
circles = defaultdict(deque)  # 반지름 별 원판에 적힌 숫자
commands = []  # 회전 명령 리스트
for i in range(1, n + 1):
    circle_nums = list(map(int, read().split()))
    deq = deque()
    for j in range(m):
        temp = [circle_nums[j], True]
        deq.append(temp)
    circles[i] += deq

for _ in range(t):
    commands.append(tuple(map(int, read().split())))


# print("initial circle", circles)
# defaultdict(<class 'collections.deque'>, {1: deque([[1, True], [1, True], [2, True], [3, True]]), 2: deque([[5, True], [2, True], [4, True], [2, True]]), 3: deque([[3, True], [1, True], [3, True], [5, True]]), 4: deque([[2, True], [1, True], [3, True], [2, True]])})

for command in commands:
    x, d, k = command  # x : x의배수인 원판선택 / d : 0(시계),1(반시계) / k : 회전횟수

    for radius, nums in circles.items():
        if radius % x == 0:
            if d == 0:
                nums.rotate(k)
            else:
                nums.rotate(-k)

    # print(circles)

    is_exist = is_exist_num(circles)
    is_delete = False  # 인접한 수 지웠는지 체크하는 플래그 변수

    # 원판에 수가 남아있는 경우
    if is_exist:
        # 수평인접 (같은 원판)
        for nums in circles.values():
            # print("수평인접 before", nums)
            # ex) deque([[2, True], [5, True], [2, True], [4, True]])
            if len(nums) >= 2:
                i, j = 0, 1
                while i <= len(nums) - 2 and j <= len(nums) - 1:
                    if nums[i][0] and nums[j][0] and nums[i][0] == nums[j][0]:
                        nums[i][1] = False
                        nums[j][1] = False
                        is_delete = True
                    i += 1
                    j += 1
                # 마지막 원소 처리
                if nums[0][0] and nums[-1][0] and nums[0][0] == nums[-1][0]:
                    nums[0][1] = False
                    nums[-1][1] = False
                    is_delete = True
            # print("수평인접체크 after", nums)

        # 수직인접 (다른 원판인데 같은 위치)
        verticals = [[] for _ in range(m)]
        for nums in circles.values():
            for i in range(len(nums)):
                verticals[i] += [nums[i]]

        # print("수직인접 before", verticals)

        for vertical in verticals:
            if len(vertical) >= 2:
                i, j = 0, 1
                while i <= len(vertical) - 2 and j <= len(vertical) - 1:
                    if vertical[i][0] and vertical[j][0] and vertical[i][0] == vertical[j][0]:
                        vertical[i][1] = False
                        vertical[j][1] = False
                        is_delete = True
                    i += 1
                    j += 1
            # print("수직인접 after", vertical)

        # print("after 수평,수직 체크", circles)

        # 인접하면서 같은 수가 있는 경우 (지워야 할 숫자가 있는 경우)
        if is_delete:
            for value in circles.values():
                for num_lst in value:
                    if not num_lst[1]:
                        num_lst[0] = 0  # 삭제한다는 의미
        # 인접하면서 같은 수가 없는 경우
        else:
            total = 0
            cnt = 0
            for value in circles.values():
                for num_lst in value:
                    if num_lst[1]:
                        total += num_lst[0]
                        cnt += 1
            aver = total / cnt
            # print("aver", aver)

            for value in circles.values():
                for num_lst in value:
                    if num_lst[1]:  # 이거 추가했어야함
                        if num_lst[0] > aver:
                            num_lst[0] -= 1
                        elif num_lst[0] < aver:
                            num_lst[0] += 1

        # print("회전 후 최종 원판", circles)
        # print("is_delete", is_delete)


# 최종 계산
total = 0
for value in circles.values():
    for num_lst in value:
        if num_lst[1]:
            total += num_lst[0]

print(total)
