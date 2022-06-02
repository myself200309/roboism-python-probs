string = input()
int_lst=[str(x) for x in range(10) ] 
res = 0

for i in string:
    if i in int_lst:
        res+=int(i)
print(res)
        
