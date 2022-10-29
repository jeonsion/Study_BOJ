#나이순 정렬
#정렬의 종류 : 선택정렬, 버블정렬, 삽입정렬 / 힙정렬 퀵정렬 병합정렬
#병합정렬을 이용해보자


#입력받기
N = int(input())

#딕셔너리들을 저장할 빈 리스트 생성
dict_list =[]
for i in range(N):
    #딕셔너리를 저장할 빈 딕셔너리 생성
    dict = {}
    #key와 name 값 입력받기
    age, name = input().split()
    age = int(age)
    #딕셔너리에 key, name 할당
    dict['age'] = age
    dict['name'] = name
    #딕셔너리 리스트에 딕셔너리 추가
    dict_list.append(dict)
    
#중간 출력결과
#[{21: 'junkyu'}, {21: 'dohyun'}, {20: 'sunyoung'}]
    
#파이썬 내장함수 sorted를 사용하여 정렬하기
# 1. iterable에는 list, str, dict등을 넣을 수 있 음
# 2. key에는 각 요소를 비교하는데 사용될 기준을 정하는 함수. 이때 함수는 인자하나를 받으며 정렬
#    기준이 될 키를 반환하는 함수 -> lambda  
#sorted(iterable, key = None, reverse = False) 

#정렬
result = sorted(dict_list, key = lambda x:x['age'], reverse = False)
#딕셔너리 리스트 안에 각각의 딕셔너리에 접근후 정렬된 age와 name 출력
for i in result:
    print(i['age'], i['name'])
    