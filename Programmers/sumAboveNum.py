def result(a,b):
    answer=0
    if a>b:
       a,b = b,a
    for i in range(a,b+1):
        answer += i
    return answer

a = int(input())
b = int(input())
print(result(a,b))