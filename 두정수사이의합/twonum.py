def solution(a, b):
    count=0
    
    if a<b:
        for i in range(a+1, b): count+=i
    elif a>b:
        for i in range(b+1, a): count+=i
    else: count+=a

    return count


a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(solution(a,b))