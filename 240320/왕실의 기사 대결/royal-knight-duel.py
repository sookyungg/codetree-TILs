from collections import deque
import copy

l,n,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(l)] # 맵 정보

info=[[0]*l for _ in range(l)]  # 맵 기사 정보
move=[(-1,0),(0,1),(1,0),(0,-1)] # 이동
knight=[[] for _ in range(n+1)] # 기사들 좌표
blood=[0]
origin_blood=[] 

init=[[0]*l for _ in range(l)] 

## init
# 말 초기 정보
for i in range(1,n+1):
    r,c,h,w,k=map(int,input().split())
    blood.append(k)

    info[r-1][c-1]=i
    for j in range(h):
        #info[r-1+j][c-1]=i
        knight[i].append([r-1+j,c-1])

    for k in range(1,w):
        #info[r-1][c-1+k]=i
        knight[i].append([r-1,c-1+k])

origin_blood=copy.deepcopy(blood)
new_knight=copy.deepcopy(knight)



for _ in range(t):
    i,d=map(int,input().split())
    q=deque()
    q.append(i)

    info=copy.deepcopy(init)
    for k in range(len(new_knight)):
        for s in range(len(new_knight[k])):
            info[new_knight[k][s][0]][new_knight[k][s][1]]=k
   
    flag=False
    tmp=[]
    while q:
        now_knight=q.popleft()
        dx=move[d][0]
        dy=move[d][1]
        
        for k in range(len(new_knight[now_knight])):
            nx=new_knight[now_knight][k][0]+dx
            ny=new_knight[now_knight][k][1]+dy

            
            if 0<=nx<l and 0<=ny<l:
                new_knight[now_knight][k][0]=nx
                new_knight[now_knight][k][1]=ny

                if board[nx][ny]==2:
                    flag=True
                    break 

                elif board[nx][ny]!=2 and info[nx][ny]!=0:
                    if info[nx][ny] not in q and info[nx][ny]!=now_knight:
                        q.append(info[nx][ny])
                        tmp.append(info[nx][ny])
                

            else:
                flag=True
                break
        
        if flag==True:
            new_knight=copy.deepcopy(knight)
            blood=copy.deepcopy(origin_blood) 
            break
        
    
    #print(i,d,new_knight,flag)

   
    if flag==False:

        for k in range(1,len(new_knight)):
            for s in range(len(new_knight[k])):
                if board[new_knight[k][s][0]][new_knight[k][s][1]]==1 and k in tmp:
                    blood[k]-=1
                    if blood[k]<=0:
                        new_knight[k]=[]
#print(new_knight)   
#print(origin_blood)
#print(blood)

sum=0
for i in range(len(origin_blood)):
    if blood[i]>0:
        sum+=origin_blood[i]-blood[i]
print(sum)