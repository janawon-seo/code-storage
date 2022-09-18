
def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multi(x, y):
    return x * y
def divi(x, y):
    return x / y

#def calc(x, y):
    #return x + y, x - y, x * y, x / y

#num1 = int(input(' 첫번째 숫자 : '))
#num2 = int(input(' 두번째 숫자 : '))
#oper = (input(' +, -, *, / : '))

def calc(num1, num2, oper):

    if oper == '+':
        print(plus(num1, num2))   
    elif oper == '-':
        print(minus(num1, num2))
    elif oper == '*':
        print(multi(num1, num2)) 
    elif oper == '/':
        if num2 == 0:
            print('0으로 나눌수 없습니다.')
        else :
            print(divi(num1, num2))       
    else:
        print('잘못 입렵하셨습니다.')    
    
        
      
 