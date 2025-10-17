# n=input().split(",")
# l=[int(item) for item in n]
# a=[]
# for i in l:
#     if i in a:
#         continue
#     else:
#         a.append(i)
# print(a)
n=input().split(",")
l=[int(a) for a in n]
s=set(l)
b=list(s)
print(b)