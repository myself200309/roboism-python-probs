arra = list(map(int, input().split()))
fk_ar = []

for x in range(len(arra)):
    if arra[x] in fk_ar:
        print(arra[x])
        break
    else:
        fk_ar.append(arra[x])
