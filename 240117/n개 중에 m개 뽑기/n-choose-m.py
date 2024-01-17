n,m=map(int, input().split())

answer=[]

def choose(cur,cnt):
    if cur==n+1:
        if cnt==m:
            for e in answer:
                print(e, end=' ')
            print()
        return

    answer.append(cur)
    choose(cur+1,cnt+1)
    answer.pop()

    choose(cur+1,cnt)
    return

choose(1,0)