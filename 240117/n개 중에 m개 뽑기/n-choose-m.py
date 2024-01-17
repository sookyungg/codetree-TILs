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
    # cur에 해당하는 숫자를 사용하였을 때의 경우를 탐색
    choose(cur+1,cnt+1)
    answer.pop()

    # cur에 해당하는 숫자를 사용하지 않았을 때의 경우를 탐색
    choose(cur+1,cnt)
    return

choose(1,0)