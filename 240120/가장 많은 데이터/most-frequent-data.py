n=int(input())
words = [input() for _ in range(n)]
d=dict()

for word in words:
    if word in d:
        d[word]+=1
    else:
        d[word]=1

# print(d)
print(d[max(d)])