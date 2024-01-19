n=int(input())
d=dict()
for _ in range(n):
    command=list(input().split())
    if command[0]=='add':
        d[int(command[1])]=int(command[2])
    if command[0]=='find':
        if int(command[1]) in d:
            print(d[int(command[1])])
        else:
            print(None)
    if command[0]=='remove':
        d.pop(int(command[1]))