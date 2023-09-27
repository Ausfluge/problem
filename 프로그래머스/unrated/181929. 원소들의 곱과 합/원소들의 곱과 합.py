def solution(num_list):
    answer = 0
    multi = 1
    sum = 0
    
    for i in num_list:
        multi *= i
        sum += i
    
    if multi < sum * sum :
        return 1
    else :
        return 0
    
    return answer