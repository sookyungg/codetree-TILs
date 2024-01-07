# 완전탐색 구현 방법
# 1. for문 기반으로 구현
# 2. 재귀함수 기반의 백트래킹
n=int(input())
answer=0
arr=[list(map(int,input().split())) for _ in range(n)]

for x in range(n-2):
    for y in range(n-2):
        tmp_ans=0
        for i in range(3):
            for j in range(3):
                if arr[i+x][j+y]==1:
                    tmp_ans+=arr[i+x][j+y]                
        answer=max(answer, tmp_ans)    
        
print(answer)