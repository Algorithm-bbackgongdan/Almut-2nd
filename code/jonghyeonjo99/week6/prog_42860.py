def solution(name):
    answer = 0
    for i in name:
        k = ord(i)-65
        if(k <= 12):
            answer += k
        else:
            answer += k-(2*(k-13))
    
    l = len(name)-1
    for i in range(0,len(name)):
        index = i +1
        while(index < len(name) and name[index] == 'A'):
            index+=1
        l = min(l, i*2 + len(name) - index)
        l = min(l, (len(name)-index)*2 + i)
    
    return answer + l