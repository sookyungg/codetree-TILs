from collections import deque

n=int(input())
visited=[]

def bfs(x):
    q=deque()
    q.append((x,0))
    visited.append(n)

    while q:
        cx, cnt=q.popleft()
        for i in range(4):
            if cx==1:
                return cnt
            if i==0:
                if cx-1 not in visited:
                    nx=cx-1
                    q.append((nx,cnt+1))
                    visited.append(nx)
            if i==1:
                if cx+1 not in visited:
                    nx=cx+1
                    q.append((nx,cnt+1))
                    visited.append(nx)
            if i==2:
                if cx%2==0 and cx//2 not in visited:
                    nx=cx//2
                    q.append((nx,cnt+1))
                    visited.append(nx)
            if i==3:
                if cx%3==0 and cx//3 not in visited:
                    nx=cx//3
                    q.append((nx,cnt+1))
                    visited.append(nx)

print(bfs(n))