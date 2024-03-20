from collections import deque

MAX_N=31
MAX_L=41
dx=[-1,0,1,0]
dy=[0,1,0,-1]

info=[[0]*MAX_L for _ in range(MAX_L)]
origin_k=[0]*MAX_N

r=[0]*MAX_N
c=[0]*MAX_N
h=[0]*MAX_N
w=[0]*MAX_N
k=[0]*MAX_N

nr=[0]*MAX_N
nc=[0]*MAX_N
dmg=[0]*MAX_N

is_moved=[False]*MAX_N

l,n,q=map(int,input().split())
for i in range(1,l+1):
    info[i][1:]=map(int,input().split())

for i in range(1,n+1):
    r[i],c[i],h[i],w[i],k[i]=map(int,input().split())
    origin_k[i]=k[i]


def try_movement(idx,d):
    q=deque()
    is_pos=True

    #초기 세팅
    for i in range(1,n+1):
        dmg[i]=0
        is_moved[i]=False
        nr[i]=r[i]
        nc[i]=c[i]

    q.append(idx)
    is_moved[idx]=True

    while q:
        x=q.popleft()
        nr[x]+=dx[d]
        nc[x]+=dy[d]

        #경계를 벗어나는지 체크 
        if nr[x]<1 or nc[x]<1 or nr[x]+h[x]-1>l or nc[x]+w[x]-1>l:
            return False

        #벽이랑 충돌하는지 + dmg
        for i in range(nr[x],nr[x]+h[x]):
            for j in range(nc[x],nc[x]+w[x]):
                if info[i][j]==1:
                    dmg[x]+=1
                if info[i][j]==2:
                    return False

       
        
        #다른 조각이랑 충돌하는지 충돌하면 append
        for i in range(1,n+1):
            if is_moved[i] or k[i]<=0:
                continue
            if r[i]>nr[x]+h[x]-1 or nr[x]>r[i]+h[i]-1:
                continue
            if c[i]>nc[x]+w[x]-1 or nc[x]>c[i]+w[i]-1:
                continue
            
            is_moved[i]=True
            q.append(i)

    dmg[idx]=0
    return True



for _ in range(q):
    idx,d=map(int,input().split())
    if k[idx]<=0:
        continue
    if try_movement(idx,d):
        
        for i in range(1,n+1):
            r[i]=nr[i]
            c[i]=nc[i]
            k[i]-=dmg[i]

# print(origin_k)
# print(k)


ans=sum([origin_k[i]-k[i] for i in range(1,n+1) if k[i]>0])
print(ans)