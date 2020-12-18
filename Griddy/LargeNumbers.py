#tip!
#idx 가 다르면 다른 수로 간주하니, 가장 큰 수와 두번째로 큰 수만 필요

#정수형 n, m, k 를 공백을 구분하여 입력받기.
#n = 입력받을수, m = 최종 덧셈 횟수 k = 반복허용치.
#map()은 py에서 data를 한꺼번에 받을 때 많이 이용.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

#정렬
data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m-=1

print(result)
