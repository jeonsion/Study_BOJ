#나이순 정렬_2

#입력받기
N = int(input())

#리스트 생성
result = []
#반복문으로 각 케이스를 입력받음
for i in range(N):
    case = input().split()
    case[0] = int(case[0])
    #리스트에 케이스리스트를 추가
    result.append(case)
    
#result리스트를 각 케이스의[0]번째 원소를 기준으로 정렬, 오름차순
final = sorted(result, key = lambda x:x[0], reverse = False)

for i in final :
    #list형태를 Unpacking하여 출력
    print(*i)