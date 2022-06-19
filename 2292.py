
from socket import if_nameindex


n=int(input())                                  #n 입력
count =1                                        #count 를 증가시켜 벌짚한바퀴를 돌고 n이 count보다 큰지 비교할 계획
sum = 1                                         #6각형을 이용하여 한바퀴 사이클과 합과 count 의 관계를 따지기

while(True):
    print("n : {}, sum : {}, count : {}".format(n, sum, count))
    
    sum=sum+(count*6)                                   #1->6->12->18 6의 배수로 사이클의 둘레가 늘어남
    count+=1
    if(n==1):
        print(1)
        break    
    elif(n<=sum):
        print(count)
        break

