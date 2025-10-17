a=input("Enter three numbers: ")
x,y,z=a.split(",")
a=int(x)
b=int(y)
c=int(z)
if a>b and a>c:
    print(f"{a} is the largest")
elif b>c and b>a:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")