n=int(input())
arr=[]
answer=[]

b1 = [(-2, 0), (-1, 0), (1, 0), (2, 0)]    # 1번 폭탄의 피해 방향
b2 = [(-1, 0), (1, 0), (0, 1), (0, -1)]    # 2번 폭탄의 피해 방향
b3 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 3번 폭탄의 피해 방향

def init_arr(arr):
    arr=[[0]*n for _ in range(n)]

#폭발 규모 확인
def bomb_explosion(arr):
    tmp_arr=[[0]*n for _ in range(n)]
    cnt=0

    for b in range(len(arr)):
        # 탐색 위치
        nx=bomb_idx[b][0]
        ny=bomb_idx[b][1]
        tmp_arr[nx][ny]=1

        #1번 폭탄
        if arr[b]==1:
            for i in range(4):
                dx=nx+b1[i][0]
                dy=ny+b1[i][1]
                if 0<=dx<n and 0<=dy<n:
                    tmp_arr[dx][dy]=1
        #2번 폭탄
        if arr[b]==2:
            for i in range(4):
                dx=nx+b2[i][0]
                dy=ny+b2[i][1]
                if 0<=dx<n and 0<=dy<n:
                    tmp_arr[dx][dy]=1    
        #3번 폭탄        
        if arr[b]==3:
            for i in range(4):
                dx=nx+b3[i][0]
                dy=ny+b3[i][1]
                if 0<=dx<n and 0<=dy<n:
                    tmp_arr[dx][dy]=1

    # 초토화된 곳 count
    for i in range(n):
        for j in range(n):
            if tmp_arr[i][j]==1:
                cnt+=1

    answer.append(cnt)
            

#폭탄 종류 결정해서 조합 만들기
def bomb_list(cur):
    if cur==bomb_cnt:
        #피해 규모 확인
        bomb_explosion(arr)
        return 

    for i in range(1,4):
        arr.append(i)
        bomb_list(cur+1)
        arr.pop()
    return

## main 실행 부분
bomb_arr=[list(map(int,input().split())) for _ in range(n)]
bomb_cnt=0
bomb_idx=[]
 

#폭탄 위치
for i in range(n):
    for j in range(n):
        if bomb_arr[i][j]==1:
            bomb_cnt+=1
            bomb_idx.append([i,j])

bomb_list(0)
print(max(answer))