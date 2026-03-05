n=int(input("Enter a number:"))
for i in range(2,n):
   if(n%i==0):
      break
   flag=0
if flag==0:
   print("Prime number")
else:
   print("Not a Prime number")
