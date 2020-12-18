#리스트가 있는 경우 순서와 리스트 값을 전달.
# for i 에 순서(i+1) name에 이름 전달. 
names = ['다미','철수','영희']
for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))