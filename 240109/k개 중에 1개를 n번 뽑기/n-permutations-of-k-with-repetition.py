k, n = map(int, input().split())
answer=[]

def makeNum(cur):
    if cur==n+1:
        for e in answer:
            print(e,end=' ')
        print()
        return
    
    for i in range(1,k+1):
        answer.append(i)
        makeNum(cur+1)
        answer.pop()

    return


makeNum(1)