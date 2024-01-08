# 재귀함수
# 1. 종료조건
# 2. 재귀호출

k,n=map(int,input().split())
arr=[]

def makeNum(cnt):
    if cnt==n:
        for num in arr:
            print(num, end=' ')
        print()
        return
    
    for i in range(1,k+1):
        if cnt>=2 and i==arr[-1] and i==arr[-2]:
            continue
        else:
            arr.append(i)
            makeNum(cnt+1)
            arr.pop()


makeNum(0)