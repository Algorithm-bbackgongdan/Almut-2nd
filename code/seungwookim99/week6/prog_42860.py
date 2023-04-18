# 실패한 코드

from collections import defaultdict

alphabets_str = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabets = defaultdict(int)


def min_up_down(target):
    idx = alphabets[target]
    return min(idx, 26 - idx)


def solution(name):
    global answer
    answer = int(1e9)
    diff_num = 0
    name_list = list(name)
    # init
    for i, c in enumerate(alphabets_str):
        alphabets[c] = i
    for c in name_list:
        if c != "A":
            diff_num += 1
    # 첫 문자가 'A'가 아니라면
    cnt = 0
    if name_list[0] != "A":
        cnt = min_up_down(name_list[0])
        diff_num -= 1
        name_list[0] = "A"

    def shortest_steps(curr, dir):
        cnt = 0
        while True:
            curr += dir
            cnt += 1
            if curr == len(name):
                curr = 0
            elif curr == -1:
                curr = len(name) - 1
            if name[curr] != "A":
                break
        return (curr, cnt)

    def dfs(curr, cnt, d_num):
        global answer
        if d_num == 0:
            answer = min(answer, cnt)
            return

        # left
        next, lr_step = shortest_steps(curr, -1)
        ud_step = min_up_down(name_list[next])
        tmp = name_list[next]
        name_list[next] = "A"
        dfs(next, cnt + lr_step + ud_step, d_num - 1)
        name_list[next] = tmp

        # right
        next, lr_step = shortest_steps(curr, 1)
        ud_step = min_up_down(name_list[next])
        tmp = name_list[next]
        name_list[next] = "A"
        dfs(next, cnt + lr_step + ud_step, d_num - 1)
        name_list[next] = tmp

        return

    dfs(0, cnt, diff_num)
    return answer + cnt
