def solution(d, buget):
    cost = 0 #가격을 0으로 초기화
    count = 0 #수를 0으로 초기화
    d.sort
    for i in range(len(d)):
        cost += d[i]
        count += 1
        if buget == cost:
            return count
        elif buget != cost:
            while cost <= buget:
                count += 1
            return count
        

d = input().split()
buget = int(input())
solution(d, buget)

