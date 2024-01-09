n,m,k=map(int,input().split())
jump=list(map(int,input().split()))
arr=[]
ans=[]

def calc(arr):
    score=[0]*k
    cnt=0
    for i in range(len(arr)):
        score[arr[i]]+=jump[i]
    #print(score)
    for s in score:
        if s>=m:
            cnt+=1
    ans.append(cnt)
    

def makelist(cur):
    if cur==n:
        calc(arr)
        return
    for i in range(0,k):
        arr.append(i)
        makelist(cur+1)
        arr.pop()
    return

makelist(0)
print(max(ans))