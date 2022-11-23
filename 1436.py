#영화감독 숌
n = int(input())
a = 666
cnt = 0

while range(n):                                 #n이 2일 때를 가정해보자
    print("while문 {}번 실행".format(cnt))
    cnt+=1
    if "666" in str(a):                     #a는 666이기 때문에 처음에 먼저 if문에 들어감
        n -= 1                              #n을 1만큼 줄인다.
    a += 1                                  #다음에 또 연속된 666이 포함되려면 1을 1000번 더한 1666일때.
    #print(a)                                #그때까지 a에1씩 더한다. 

print(a-1)

