n, c= map(int, input().split())
t=list(map(int, input().split()))   


dic= dict()                     

for i in t:
    if i not in dic  :  
        dic[i]=0
    else    :
        dic[i]  +=1     

#key = lambda x : x[1] : 원래는 key기준으로 정렬이지만 람다를 이용하여 value기준 정렬
#파이썬 정렬함수는 안정정렬(입력받은 순서대로 정렬) 즉, 여기서 value가 같을 시 먼저 입력받은 순서를
#고려해서 정렬한다.
sdict=sorted(dic.items(), key= lambda x :x[1], reverse=True)

for a, b in sdict :
    print((str(a)+" ")*(b+1), end="")