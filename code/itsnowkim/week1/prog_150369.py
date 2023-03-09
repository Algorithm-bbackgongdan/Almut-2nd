def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 마지막까지 배달해야 하는 index
    d_i = 0
    for i in reversed(range(n)):
        if deliveries[i] != 0:
            d_i = i
            break
    
    # 마지막까지 수거해야 하는 index
    p_i = 0
    for i in reversed(range(n)):
        if pickups[i] != 0:
            p_i = i
            break
    
    # maximum index
    m_i = max(d_i, p_i)
    if m_i == 0:
        return answer
    
    # 일단 가장 멀리 가야 함 - 뒤에서부터 배달할 수 있는 최대만큼 배달, 수거도 마찬가지
    while True:    
        if m_i == -1:
            break
        answer += (m_i+1)*2
        
        temp_del = 0
        # 배달
        while d_i >=0 and temp_del <= cap:
            if temp_del + deliveries[d_i] <= cap:
                temp_del += deliveries[d_i]
                deliveries[d_i] = 0
                d_i -= 1
            elif temp_del < cap:
                deliveries[d_i] -= (cap - temp_del)
                temp_del = cap
                break
            else:
                break
        # 수거
        temp_pick = 0
        while p_i>= 0 and temp_pick <= cap:
            if temp_pick + pickups[p_i] <= cap:
                temp_pick += pickups[p_i]
                pickups[p_i] = 0
                p_i -= 1
            elif temp_pick < cap:
                pickups[p_i] -= (cap-temp_pick)
                temp_pick = cap
                break
            else:
                break
        
        m_i = max(d_i,p_i)

    return answer
# solution(4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0])
# solution(2,	7,	[1, 0, 2, 0, 1, 0, 2],	[0, 2, 0, 1, 0, 2, 0])