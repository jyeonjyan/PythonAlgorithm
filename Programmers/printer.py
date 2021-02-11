def solution(properties, location):
    # 해당 location의 값
    locationValue = properties[location]
    first = max(properties)
    print(properties.index(first))
    

array = [2,1,3,2]
location = 2
solution(array, location)