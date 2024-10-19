a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

operator = input("Enter the operator")

if operator=="+":
    print("The sum of 2 numbers is ", a+b)

elif operator =="-":
    print("a-b=",a-b)

elif operator =="*":
    print("a*b=",a*b)

elif operator =="/":
    if b == 0:
        print("Invalid")
    else: 
        print("a/b=",a/b)

else:
    print("Invalid input")
    
