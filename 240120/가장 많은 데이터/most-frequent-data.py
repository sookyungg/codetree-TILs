n=int(input())
d=dict()

for _ in range(n):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1

print(d)
print(d[max(d)])