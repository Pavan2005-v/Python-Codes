n=input().split(",")
a=[int(item) for item in n]
c=0
d=int(input("Enter element to be searched: "))
for i in a:
    if i==d:
        c+=1
print("No of occurences: ",c)
