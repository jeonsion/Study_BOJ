#균형잡힌세상
#스택이용
#입력의 종료 조건으로   "." 이 들어온다.

result = []
while True:
    #입력받기
    str = input().rstrip()
    stack = []
    if str ==".":
        break
    
    for i in str:
        if(i == "(" or i=="["): #여는 괄호를 만났을 때
            stack.append(i) #일단 추가하기
        elif(i == ")"):     #닫는 소괄호일 때
            #stack이 비어있다면
            if(len(stack)!=0 and stack[-1]=="("):
                stack.pop()
            else:
                stack.append(i) #스태의 짝이 안맞더라도 집어넣어서 오류 고의적으로 발생시킬거다
        elif(i == "]"):
            #stack이 비어있다면
            if(len(stack)!=0 and stack[-1]=='['):
                stack.pop()
            else:
                stack.append(']')

    if(len(stack)==0):
        print("yes")
    else:
        print("no")
