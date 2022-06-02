def encrypt(card_no):            
    dummy = card_no
    count = 0
    string = ''
    while dummy>0:
        count+=1
        if count<5:
            dig = str(dummy%10)
        else:
            dig ='*'
        string = dig+ string
        
        dummy = dummy//10
    return string


card_no = int(input('Enter card no.')) # limitation first digit has to be non zero
print(encrypt(card_no))


def encrypt_impr(card_no):
    str1 = card_no [-5:-1]
    return "*"*(len(card_no)-4)+str1


card_no1 = input()
print(encrypt_impr(card_no1))
