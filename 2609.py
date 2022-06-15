



num1, num2 = map(int, input().split())

if(num1 >num2) :
    max = num1
    min = num2
else :
    max = num2
    min = num1

for i in range(min, 0, -1)  :
    if((num1%i ==0) and (num2%i==0)) :
        gcd = i
        break

print(gcd)        
print(int((num1*num2)/gcd))        




    

