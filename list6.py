l=list(map(int,input("Enter 10 integers to be in the list:").split()))
e=[]
o=[]
for i in l:
   if i%2==0:
      e.append(i)
   else:
      o.append(i)
print("The even list is :", e)
print("The odd list is :" ,o)
