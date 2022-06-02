def calc(num1, opt, num2):
    if opt == '+':
        return num1+num2
    elif opt == "-":
        return num1-num2
    elif opt=='/':
        return num1/num2
    elif opt== '.':
        return num1*num2
    else:
        return 'please enter correct operator!'
n1, n2 = map(int, input().split())
opt = input("enter +, -, /, or .:")
print(calc(n1,opt,n2))
