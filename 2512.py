n=int(input()) 
narr=list(map(int,input().split()))
narr.sort()
m=int(input())

st=0
en=max(narr)
cnt=0

if sum(narr) < m:
        print(max(narr))
else:   
    while st<=en    :
        mid=(st+en)//2
        총예산=0
        #  print("mid값 세팅 : {}".format(mid))
        for i in narr   :
            if i >mid   :
                총예산 += mid
            else    :
                총예산 +=  i
            # print("st의 값 : {}, en의 값 : {}, i의 값 : {}, mid의 값: {}, 총예산의 값 : {}".format(st, en, i, mid, 총예산))
        if m < 총예산      :
            en =mid-1
            #print("요청한 예산이 총예산보다 큼 ")
        else :
            st = mid+1
            #print("요청한 에산이 총예산보다 작음.")
    print(en)