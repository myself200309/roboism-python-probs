def count(arra,ele):
    c = 0
    for i in range(len(arra)):
        if arra[i] == ele:
            c+=1
    return c

arra = list(map(int, input().split()))
dic = {}
for x in range(len(arra)):
    if arra[x] not in dic.keys():
        dic[arra[x]] = count(arra, arra[x])
print(dic)
