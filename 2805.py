# 나무자르기
# 이분탐색
import sys
input = sys.stdin.readline


#입력받기
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))


length = 0
start = 1
end = max(tree_list)
while(start <= end):
    #각 케이스마다 legnth 초기화 후 실행
    length = 0
    mid = (start+end) // 2
    for i in tree_list:
        if(i>mid):  #i가 mid보다 커야 i - mid를 했을 때 남는 나무가 발생
            length += i-mid
        if length > M:
            break
    #만약 length 가 필요한 나무의 길이 M보다 크면 mid의 오른쪽 범위에서 탐색
    if length < M:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)
