a=input("Enter a string: ")
b=a.lower()
c=0
for i in b:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        c+=1
print("Number of vowels: ",c)
