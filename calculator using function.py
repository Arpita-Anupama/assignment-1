def addition(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("select operation 1 for addition and 2 for sustraction")
op=int(input("1 or 2:"))
if op==1:
    print(x,"+",y,"=",addition(x,y))
elif op==2:
    print(x,"-",y,"=",substraction(x,y))
else:
    print("invalid")
