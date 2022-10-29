#좌표정렬하기
#2차평면위에 좌표 x,y가 주어지면 오름차순으로 정렬하는 프로그램 작성

#점의 개수 입력받기
N = int(input())

#점의 좌표를 입력받을 리스트 선언
A_list = []
#반복문으로 N개의 점의 좌표 입력받기
for i in range(N):
    XY = list(map(int, input().split()))
    A_list.append(XY)
    
#파이썬 내장함수 sorted로 정렬하기 
#중점적으로 봐야할 점은 key값의 람다가 x[0], x[1]인 것은 x[0]을 기준으로 먼저 오름차순 정렬 그다음은 x[1]기준으로 정렬한다.
result_list = sorted(A_list, key = lambda x:(x[0], x[1]), reverse = False)

#출력
for i in result_list:
    print(*i)