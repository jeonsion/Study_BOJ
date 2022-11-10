#숫자카드 2
#문제 : 상근이가 숫자카드를 몇개 가지고 있는지 출력
#N은 상근이가 가지고 있는 카드개수
#M은 상근이가 몇개 가지고 있는 숫자 카드인지 구해야할 M개의 정수들
# 아이디어 : 1. 상근이가 가지고있는 카드를 정렬한다. 2. 경계값을 찾아 시작점과 끝 점의 차이로 개수를 카운트한다.
# 접근 방법 : 문제에서 주어진 입력의 개수는 500,000이 넘음 -> O(N)으로 풀면 안될 것 같음, 그리고 밑에 '이분탐색'키워드를 봐버림 정렬알고리즘 이용하자
#경계값 찾는 알고리즘 연습하기(이진탐색 이용)


import sys
input = sys.stdin.readline


# 1. 기본의 이분탐색 알고리즘   O(logN)
def BSearch(start, end, array, target):
    if(start > end):
        return None
    
    mid = (start + end)//2
    if(array[mid] == target):
        return mid
    #찾으려는 값이 mid보다 왼쪽에 있음
    elif array[mid] > target:
        return BSearch(start, mid-1, array, target)
    #찾으려는 값이 mid 보다 오른쪽에 있음
    else: 
        array[mid] < target
        return BSearch(mid+1,end, array, target)

# 2. Lowwer Bound 알고리즘
# 아이디어 : 이분탐색으로 정렬 후 나오는 target의 인덱스 기준으로, 왼쪽으로 줄였을 때 target값이 달라질 때 까지 
#          반복해서 return해야할 값을 -1 해서 시작 경계값을 return한다.
def BSearch_left(start, end, array, target):
    #Base case
    if(start > end):
        return 0
    mid = (start + end) // 2
    # 값 일단 찾음
    if(array[mid] == target):
        #앞쪽 갚과 비교
        while(mid>= start and array[mid]==target):
            mid  = mid-1
        return mid+1
    elif array[mid] > target:
        return BSearch_left(start, mid-1, array, target)
    else:
        array[mid] < target
        return BSearch_left(mid+1, end, array, target)
    
    
    
def BSearch_right(start, end, array, target):
    if(start > end):
        return 0
    mid = (start + end) // 2
    # 값 일단 찾음
    if(array[mid] == target):
        #앞쪽 갚과 비교
        while(mid <= end and array[mid]==target):
           mid+=1
        return mid 
    elif array[mid] > target:
        return BSearch_right(start, mid-1, array, target)
    else: 
        array[mid] < target
        return BSearch_right(mid+1, end, array, target)
    

def BSearch_left2(start, end, array, target):
    while start<=end:
        mid = (start + end) // 2
        if(array[mid] < target):
            start = mid +1
        else:
            end = mid - 1
    return start

def BSearch_right2(start, end, array, target):
    while start <=end:
        mid = (start + end) // 2
        if(array[mid] <= target):
            start = mid +1
        else:
            end = mid -1
    return start




N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

#출력할 빈 리스트 생성

# N_list정렬 -> 이분탐새은 정렬이 전제되어야함
N_list.sort()



for i in M_list:
    #Upper bound 인덱스 - Lower bound 인덱스 결과 값으로 원소의 개수를 출력한다.
    print(BSearch_right2(0, len(N_list)-1, N_list, i)- BSearch_left2(0, len(N_list)-1, N_list, i), end = ' ')

