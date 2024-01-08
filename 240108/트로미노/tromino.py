n,m=map(int,input().split())
arr=[[0]*m for _ in range(n)]

for i in range(n):
    arr[i]=list(map(int, input().split()))

   

def blockchk(n, m, arr):
    
    blocksum=0
    answer=0
    
    #L자 블록
    Lblock=[[(0,0),(1,0),(1,1)], [(0,1),(1,0),(1,1)], [(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,1)]]
    for l in Lblock:
        for x in range(n-1):
            blocksum=0
            for y in range(m-1):
                blocksum=arr[x+l[0][0]][y+l[0][1]]+arr[x+l[1][0]][y+l[1][1]]+arr[x+l[2][0]][y+l[2][1]]
                #print(arr[x+l[0][0]][y+l[0][1]], arr[x+l[1][0]][y+l[1][1]], arr[x+l[2][0]][y+l[2][1]])
                #print(blocksum)
                answer=max(answer,blocksum)

    #I자 블록
    #Iblock=[[(0,0),(0,1),(0,2)], [(0,0),(1,0),(2,0)]]
    i=[(0,0),(0,1),(0,2)]
    for x in range(n):
        blocksum=0
        for y in range(m):
            if y+2<m:
                #print(arr[x+i[0][0]][y+i[0][1]], arr[x+i[1][0]][y+i[1][1]], arr[x+i[2][0]][y+i[2][1]])
                blocksum=arr[x+i[0][0]][y+i[0][1]]+arr[x+i[1][0]][y+i[1][1]]+arr[x+i[2][0]][y+i[2][1]]
            answer=max(answer,blocksum)

    i=[(0,0),(1,0),(2,0)]
    for x in range(n):
        blocksum=0
        for y in range(m):
            if x+2<n:
                #print(arr[x+i[0][0]][y+i[0][1]], arr[x+i[1][0]][y+i[1][1]], arr[x+i[2][0]][y+i[2][1]])
                blocksum=arr[x+i[0][0]][y+i[0][1]]+arr[x+i[1][0]][y+i[1][1]]+arr[x+i[2][0]][y+i[2][1]]
                #print(blocksum)
            answer=max(answer,blocksum)
    
    print(answer)

blockchk(n, m, arr)