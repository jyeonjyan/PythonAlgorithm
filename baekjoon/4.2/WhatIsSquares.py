def solution(min, max):
    result = 0
    for i in range(min, max+1):
        if (int (i**0.5) ** 2 == i) == False:
            result += 1
    return result
