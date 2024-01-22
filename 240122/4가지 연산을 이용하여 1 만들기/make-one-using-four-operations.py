from collections import deque

n=int(input())

def bfs(x):
    q=deque()
    q.append((x,0))
    while q:
        cx, cnt=q.popleft()
        for i in range(4):
            if cx==1:
                return cnt
            if i==0:
                nx=cx-1
                q.append((nx,cnt+1))
            if i==1:
                nx=cx+1
                q.append((nx,cnt+1))
            if i==2:
                if cx%2==0:
                    nx=cx//2
                    q.append((nx,cnt+1))
            if i==3:
                if cx%3==0:
                    nx=cx//3
                    q.append((nx,cnt+1))

print(bfs(n))