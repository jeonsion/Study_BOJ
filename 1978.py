#주어진 n개 수 중에서 소수가 몇개인지 찾기
#입력 : 첫줄에 수의 개수 n n은 100이하, 다음으로 n개의 수ㅏㄱ 주어지는데 수는 1,000 이하의 자연수

#아이디어 : 1000이하의 수를 False으로 초기화 한다음에 소수를 모두 True로 변환 및 저장
import sys
input = sys.stdin.readline


#전체 배열 A에 숫자 할당하기
A = [i for i in range(1001)]
#1은 소수가 아니므로 False할당 후 시작
A[1] = False


#2부터 1000까지 반복문 실행
for i in range(2, 1001):
    
    #이미 삭제된 요소는 건너뜀 A[i] == False인 경우를 제외하고 실행
    if(A[i] !=False):
        mul = 2
        #자기 자신을 제외한 배수들 False할당(삭제)
        while(mul * i < 1001):
            A[mul*i] = False
            mul+=1


#입력받기
N = int(input())
M = list(map(int, input().split()))

#소수의 개수 카운트할 변수 선언
count = 0

for i in M:
    #요소가 False가 아니면 count+=1
    if(A[i]!=False):
        count+=1
print(count)

