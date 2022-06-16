t = int(input())


for j in range(t):
    count_w = 1
    r=101                                                   #첫번째 손님에게 드리는 경우의 수
    #print("*******r 시작 : {}*********".format(r))
    h, w, n = map(int, input().split())
    for i in range(1, n):                                   #for문을 통하여 '다음사람'에게 줄 수 있는 경우의 수 를 구한다
       # print("{}번째 손님 : 에게 드리는 방 {}".format(i, r))
        if(i%h==0):
            count_w+=1
            r=100+count_w
        #    print("r(i%h) : {}".format(r))
        else:
            r+=100
        #    print("r : {}".format(r))
        
    print(r)