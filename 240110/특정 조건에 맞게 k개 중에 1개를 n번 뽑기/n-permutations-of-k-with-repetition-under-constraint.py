k,n=map(int,input().split())
arr=[]
    
def makearr(cur):
    if cur==n:
        cnt = 1
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                cnt += 1
                if cnt == 3:
                    return
            else:
                cnt = 1
        for el in nums:
            print(el, end=" ")
        print()
        return 

    for i in range(1,k+1):
        arr.append(i)
        makearr(cur+1)
        arr.pop()

makearr(0)