n=int(input())
answer=0
arr=[[0]*n for _ in range(n)]

for i in range(n):
    arr[i]=list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        tmp_ans=0
        if i+2<n and j+2<n:
            for n in range(3):
                for m in range(3):
                    tmp_ans+=arr[i+n][j+m]
                
            answer=max(tmp_ans,answer)    
        
        
print(answer)