
def find_max(num1, num2, num3):
    #이어서 하기
    #조건문에 max를 저장하면서 이 max는 최대로 m을 초과하면 안됨 and연산자 이용하기


n, m = map(int, input().split())
card = list(map(int,input().split()))
max = 0

max = 0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            find_max(card[i], card[j], card[k])

