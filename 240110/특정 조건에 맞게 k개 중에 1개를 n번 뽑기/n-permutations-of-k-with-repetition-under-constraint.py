k,n=map(int,input().split())
arr=[]
    
def makearr(cur):
    if cur==n:
        if [arr[0]]*n != arr:
            #print(arr)
            for a in arr:
                print(a, end=' ')
            print()
        return 
    for i in range(1,k+1):
        arr.append(i)
        makearr(cur+1)
        arr.pop()

makearr(0)