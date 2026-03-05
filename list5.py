n=int(input("Enter the starting integer of the list:"))
s=int(input("Enter the step to be rised:"))
l=[n]
c=1
for i in l:
   if c<11:
    l.append(n+s)
    n=n+s
    c+=1
print("The list is ",l)
l.reverse()
print("The reversed list is ",l)
