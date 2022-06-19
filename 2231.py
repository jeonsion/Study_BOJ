
def find_solution(n):               #각 자릿수의 합을 찾는 함수
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
    
    
# <중점사항>
# 1. 한지릿 수 일 때 고려 ex(8->4,6->3)
# 2. a<count 일 때는 분해합이 없는 경우 이므로 고려
    
    
    
