w = input()
sum=0
for i in range(len(w))  :
    if w[i] in "ABC"   :
        sum+=2
    elif w[i] in "DEF":
        sum +=3
    elif w[i] in "GHI":
        sum +=4
    elif w[i] in "JKL":
        sum +=5
    elif w[i] in "MNO":
        sum +=6
    elif w[i] in "PQRS":
        sum +=7
    elif w[i] in "TUV":
        sum +=8
        
    else :
        sum+=9
       


print(sum+len(w))