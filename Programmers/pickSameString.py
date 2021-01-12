def solution(s):
    pCount = 0
    yCount = 0
    
    for i in range(len(s)):
        if s[i].lower().count("p"):
            pCount += 1
        if s[i].lower().count("y"):
            yCount += 1

    if pCount == yCount:
        return True
    else:
        return False

value = input()
print(solution(value))