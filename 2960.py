n,k=map(int, input().split())
l=[True for i in range(n+1)]   #만약 n이 7일 때 0~7까지 만들어짐
cnt=1                           #카운트를 1시작으로 해야,,,이것때문에 1시간 걸림


for i in range(2, n+1)  :       #0,1,을 제외한 2부터 지우기 시작함
    if l[i]==True :              #만약 i가4 일때 이미 4는 지워졌을 상태이므로 건너뛰기 위한 조건문
        for j in range(i, n+1, i) : #i가2이고 n이 7일 때, i의 배수만큼 증가하면서 삭제
            if l[j]==False :         #공배수를 띄어넘기 위한 조건문 
                continue
        
            if cnt==k :                 #만약 카운트 값과 k값이 일치할 때 뭐지웠는지 출력
                print(j)
    
        l[j]=False               #그렇지 않은 것에 대한 리스트 요소의 삭제 
        cnt+=1                    #지웠으면 카운트 
