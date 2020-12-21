def solution(s):
    if s % 2==0 or s == 0:
        return "Even"
    else:
        return "Odd"


value = int(input())
answer = solution(value)
print(answer)
