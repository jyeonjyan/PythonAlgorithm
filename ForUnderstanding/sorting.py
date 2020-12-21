# How to 정렬

#오름차순 정렬은 sorted()함수를 사용합니다.
# a = sorted([5,2,4,1,6])
# print(a)

#입력 받은 값 정렬.
myList = list()
for i in range(0,5):
    s = input()
    myList.append(s)

myList.sort()
print(myList)

