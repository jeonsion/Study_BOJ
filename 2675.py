t=int(input())      #케이스에 개수 받기

for i in range(t)   :       #케이스 개수만큼 반복 e) t = 2
    r, s = input().split()  #r은 반복할 횟수, s 는문자열
    r=int(r)
    result=''   #문자열을 담을 공백의 변수 생성
    for j in s: #반복문으로 문자열의 요소 하나하나 접근
        result+=j*r 
    print(result)