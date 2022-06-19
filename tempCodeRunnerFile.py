
def find_solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer

a = int(input())
count = 0
sum = 0
while(True):
    sum = find_solution(count)
    sum+=count
    #print("sum : {}, count : {}".format(sum, count))
    if(a<count):
        print(0)
        break
    elif(a==sum):
        print(count)
        break
    count+=1
    
    
    
