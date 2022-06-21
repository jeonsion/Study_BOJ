#팰린드롬수/ 회문인지 아닌지 알아보기
# -> 자료구조시간에 배운 스택을 이용하여 알아보자



case = list(map(int, input()))
case_stack = list(reversed(case))

while(case!=[0]):
    
    if(case!=case_stack):
        print("no")
    else:
        print("yes")
        
    case = list(map(int, input()))
    case_stack = list(reversed(case))
        