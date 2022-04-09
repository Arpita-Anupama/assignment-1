print("calculator")
print("add=1")
print("substract=2")
ch= int(input("enter your choice(1 or 2): "))

if ch==1:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    z=x+y
    print("sum= ",z)
elif ch==2:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    z=x-y
    print("difference= ",z)
else:
    print("invalid")
