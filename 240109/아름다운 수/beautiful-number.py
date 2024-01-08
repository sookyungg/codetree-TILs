n=int(input())
ans=[]
cnt=0

def isBeautiful():
    for i in range(n):
        if i==0:
            now=ans[i]
            cnt=1
        elif now==ans[i]:
            cnt+=1
        else:
            if cnt%now==0:
                cnt=1
                now=ans[i]
                continue
            else:
                return False
    if cnt%now==0:
        return True

def makeNum(cur):
    global cnt
    if cur==n+1:
        if isBeautiful()==True:
            cnt+=1
        return cnt

    for i in range(1,5):
        ans.append(i)
        makeNum(cur+1)
        ans.pop()

makeNum(1)
print(cnt)