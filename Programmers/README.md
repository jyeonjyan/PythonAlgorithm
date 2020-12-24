## 배운점

**solution.py**
> 내가 생각했던 알고리즘
```
def solution(s):
    sLength = len(s)로 저장
    if sLength%2==0:
        return s[sLength/2], s[(sLength/2)+1]
    else:
        return [(sLength/2)+1]


list [] #배열 선언
sentence = input() #변수에 문자열 저장
list.append(sentence) #배열에 변수 대입
answer = solution(sentence) #결과값에 def solution return 값 대입
print(answer) #결과 값 출력
```
**이렇게 하면 오류가 나는 이유**
> 우선
```
TypeError: string indices must be integers
```
> 두 번째
```
sLength/2 가 아닌, (sLength//2)-1 인덱스는 0 ~ 이니깐
```

### 두 정수 사이 합 구하기
**문제설명**
> 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.  
> 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
