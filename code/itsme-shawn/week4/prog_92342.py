# 양궁대회
def solution(n, info):
    print()
    print(info)
    possible_answer = []
    result = []
    ryan_possible_info = []  # 10점 ~ 0점
    for i in range(len(info)):
        ryan_possible_info.append([0, info[i] + 1])

    print(ryan_possible_info)

    for i in range(0b11111111111 + 0b1):
        bin_to_str = ("0" * 10 + str(bin(i))[2:])[-11:]
        temp = []
        for j in range(11):
            temp.append(ryan_possible_info[j][int(bin_to_str[j])])

        result.append(temp)

    maxx = 0

    for res in result:
        apeach_score, ryan_score = 0, 0
        if sum(res) > n:
            continue
        else:
            # print("res1", res)
            for i in range(11):
                if info[i] == 0 and res[i] == 0:
                    pass
                elif info[i] < res[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i

            # print("r,a", ryan_score,apeach_score)

            if ryan_score - apeach_score >= maxx:
                maxx = ryan_score - apeach_score
                # print("res2", res)
                possible_answer.append([maxx, res])

    max_results = []

    for ans in possible_answer:
        if ans[0] == maxx:
            max_results.append(ans[1])

    # max_results.sort(key=lambda x : (-x[-1],-x[-2],-x[-3],-x[-4],-x[-5],-x[-6],-x[-7],-x[-8],-x[-9],-x[-10],-x[-11]))
    max_results.sort(key=lambda x: tuple(-x[(-1) * i] for i in range(1, 12)))
    print(max_results)
    # 예시 : [[1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0], [1, 1, 2, 3, 0, 2, 0, 0, 0, 0, 0]]

    if maxx == 0:
        return [-1]
    else:
        ans = max_results[0]
        if sum(ans) < n:
            ans[-1] += n - sum(ans)
        return ans
