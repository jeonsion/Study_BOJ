c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

a=input()
sum=0
i=0


while i < len(a)  :
    #print("i :", i)
    if a[i:i+2] in c    :
       sum +=1
       i+=2
       #print("두자리")
    elif a[i:i+3] in c:
        sum+=1
        i+=3
        #print("세자리")
    else:
        sum+=1 
        i+=1
        #print("일반문자")


print(sum)




