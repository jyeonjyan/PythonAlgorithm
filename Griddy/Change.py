# 가장 최소의 동전 개수로 1260원을 거슬러 주는 방법은?

n = 800 # 거스름돈
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count += n //coin # 해당 화폐로 거슬러 줄 수 있는 동전 개수
    n%=coin
    #print(n) # 260, 60, 10, 0 이 차례로 반환

print(count)