def solution(s):
    mystring = s
    length = len(s)
    result = []
    if length%2==0:
        result = mystring[length/2], mystring[length/2+1]
        return result
    else:
        result = mystring[length/2+1]
        return result

list = []
sentence = input()
list.append(sentence)
answer = solution(sentence)
print(answer)
