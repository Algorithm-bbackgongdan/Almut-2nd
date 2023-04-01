import math
def solution(fees, records):
    visited = [False for i in range(10000)]
    parkingTime = [0 for i in range(10000)]
    res = [0 for i in range(10000)]
    answer = []
    freeTime,freeFee,unitTime, unitFee = fees
    
    for i in range(len(records)):
        carnum = records[i][6:10]
        idx = int(carnum)

        if records[i][11:] == "IN":
            visited[idx] = True
            start_H = int(records[i][0:2])
            start_M = int(records[i][3:5])
            time = start_H * 60 + start_M
            res[idx] = time
        elif records[i][11:] == "OUT":
            visited[idx] = False
            end_H = int(records[i][0:2])
            end_M = int(records[i][3:5])
            time = end_H * 60 + end_M
            parkingTime[idx] += time - res[idx]
            
    endTime = 23 * 60 + 59
    for i in range(len(visited)):
        if visited[i] == True:
            visited[i] = False
            parkingTime[i] += endTime - res[i]
    
    for times in parkingTime:
        if times != 0:
            if times <= fees[0]:
                answer.append([parkingTime.index(times),fees[1]])
            else:
                fee = freeFee + math.ceil((times - freeTime)/unitTime) * unitFee
                answer.append([parkingTime.index(times),fee])
    sorted(answer)
    
    ans = [row[1] for row in answer]
    return ans