
a,b,v = map(int, input().split())
#낮에 a만큼 올라감, 밤에는 b만큼 미끄러짐, 높이 v

if(((v-b)%(a-b))!=0):
    print(int((v-b)/(a-b)+1))
else:
    print(int(((v-b)/(a-b))))


# tip :
# 반복문 사용하면 안됨
# 실질적으로 달팽이가 올라가는 거리는 v-b 만약
# 하루에 올라가는거리(a-b)가 매일 매일 증가하면서 v에 나눠떨어지지 않을 때는
# 1을 증가하여 준다 ->>달팽이는 낮에만 도착한다(하루증가)