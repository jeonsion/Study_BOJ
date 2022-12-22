import sys
input = sys.stdin.readline

n = int(input())    #노드 개수


n_list = [[] for i in range(0, n+1)]

#부모노드 저장하는 리스트
Parent = [0 for i in range(n+1)]


#트리 구조 생성하기
for i in range(n-1):
    s, e = map(int,input().split())
    n_list[s].append(e)
    n_list[e].append(s)

#print(n_list)

def dfs(start, tree, parent):
    for i in n_list[start]: #1번노드부터 dfs 시작
        if parent[i] == 0:  #부모노드가 정해지지 않았으면
            parent[i] = start   #부모노드로 선정 ex)1번 노드는 자기자신
            dfs(i, tree, parent)


#    1.[1] 2.[4] 3.[] 4.[1] 5.[] 6.[1] 7.[4]

dfs(1, n_list, Parent)  #dfs 시작

for i in range(2, n+1):
    print(Parent[i])


