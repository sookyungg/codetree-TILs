n=int(input())
words = [input() for _ in range(n)]
d=dict()
ans=0

for word in words:
    if word in d:
        d[word]+=1
    else:
        d[word]=1

    ans=max(ans, d[word])

print(ans)