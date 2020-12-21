def solution(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        return s[(len(s)//2) -1: len(s)//2+1]

list = []
sentence = input()
list.append(sentence)
answer = solution(sentence)

