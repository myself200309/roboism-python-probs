def doubler(string):
    arra = [char for char in string]
    nw_arra = []
    for i in range(len(arra)):
        nw_arra.append(arra[i]*2)
    return ''.join(nw_arra)

string = input('enter string to be doubled:')
print(doubler(string))
