# l=[15,2,7,25,10]
# max=l[0]
# min=l[0]
# n=len(l)
# for i in range(0,n):
#     if l[i]>max:
#         max=l[i]
#     if l[i]<min:
#         min=l[i]
# print("Maximum = ",max)
# print("Minimum = ",min)
l=[15,2,7,25,10]
l.sort()
n=len(l)
print("Maximum = ",l[n-1])
print("Minimum = ",l[0])