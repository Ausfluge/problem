def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    x = (numer1 * denom2) + (numer2 * denom1)
    y = denom1 * denom2
    
    big = max(x, y)
    
    gcd = 0
    
    for i in range(big, 0, -1):
        if y % i == 0 and x % i == 0 :
            gcd = i
            break
    
    answer = x / i, y / i
    
    
    
    return answer