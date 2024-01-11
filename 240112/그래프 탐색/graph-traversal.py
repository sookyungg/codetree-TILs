# DFS 꼭 재귀함수 이용해서 작성
# 1번부터 정점의 개수 까지 for문을 돌아야함
# 방문했는지 확인, if 조건 확인
# 1. 시작점으로부터 연결된 모든 정점을 전부 방문해야 합니다.
# 2. 이미 방문한 정점은 다시는 방문하지 않습니다.

n,m=map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [[0] for _ in range(n+1)]
res=0

for _ in range(m):
    x,y=map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    global res
    for cur in graph[v]:
        if not visited[cur]:
            visited[cur]=True
            res+=1
            dfs(cur)

visited[1]=True
dfs(1)
print(res)