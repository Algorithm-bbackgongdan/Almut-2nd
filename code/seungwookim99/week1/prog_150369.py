def findFarthestIndex(L):
    for i in range(len(L)-1, -1, -1):
        if L[i] > 0:
            break
    return i

def isWorkRemain(remainWorks):
    return remainWorks != 0

def work(workList, workIdx, cap):
    doneWorksNum = 0
    
    # 최대 cap 개수만큼 배달/수거 작업 수행
    while (workIdx >= 0) and (doneWorksNum != cap):
        if workList[workIdx] > 0:
            workList[workIdx] -= 1
            doneWorksNum += 1
        else:
            workIdx -= 1
    
    # 만약 workList[workIdx]가 0이라면, workList[workIdx] > 0 일 때 까지 workIdx 감소
    if (workIdx >= 0) and (workList[workIdx] == 0):
        while workIdx >= 0:
            if workList[workIdx] > 0:
                break
            workIdx -= 1
    
    return (doneWorksNum, workIdx)

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliverIdx = findFarthestIndex(deliveries)
    pickupIdx = findFarthestIndex(pickups)
    
    remainDeliver = sum(deliveries)
    remainPickups = sum(pickups)
    
    while (isWorkRemain(remainDeliver)) and (isWorkRemain(remainPickups)):        
        answer += 2 * (max(deliverIdx, pickupIdx) + 1)
        
        deliverDoneNum, deliverIdx = work(deliveries, deliverIdx, cap)
        pickupDoneNum, pickupIdx = work(pickups, pickupIdx, cap)
        
        remainDeliver -= deliverDoneNum
        remainPickups -= pickupDoneNum
    
    while isWorkRemain(remainDeliver):
        answer += 2 * (deliverIdx + 1)
        deliverDoneNum, deliverIdx = work(deliveries, deliverIdx, cap)
        remainDeliver -= deliverDoneNum
    
    while isWorkRemain(remainPickups):
        answer += 2 * (pickupIdx + 1)
        pickupDoneNum, pickupIdx = work(pickups, pickupIdx, cap)
        remainPickups -= pickupDoneNum
    
    return answer