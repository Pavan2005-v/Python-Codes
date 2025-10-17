num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
operator=input("Enter an operator: ")
if operator=="+":
    print(f"Addition: {num1+num2}")
elif operator=="-":
    if num1>num2:
        print(f"Subtraction: {num1-num2}")
    else:
        print(f"Subtraction: {num2-num1}")
elif operator=="*":
    print(f"Multiplication: {num1*num2}")
elif operator=="/":
    if num2!=0:
        print(f"Division: {num1/num2}")
else:
    print("Enter valid operator")
