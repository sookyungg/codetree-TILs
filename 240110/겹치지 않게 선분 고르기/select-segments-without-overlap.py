n=int(input())
line_arr=[]
arr=[]
ans=[]

for i in range(n):
    line_arr.append(list(map(int, input().split())))
line_arr.sort()

#이어지는지 체크
def line_chk(arr):
    tmp=[]
    for i in range(len(arr)):
        if arr[i]==1:
            tmp.append(line_arr[i])
    
    flag=0
    for i in range(len(tmp)-1):
        if tmp[i][-1] >= tmp[i+1][0]:
            flag=1
    if flag==0:
        ans.append(sum(arr))
    

#조합 만들기
def line_list(cur):
    if cur == n:
        line_chk(arr)
        return 
    for i in range(2):
        arr.append(i)
        line_list(cur+1)
        arr.pop()
    return

line_list(0)        
print(max(ans))