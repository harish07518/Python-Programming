def interest(p,n,ch):
   if (ch==1):
      s=(p*n*12)/100
      
   elif (ch==2):
      s=(p*n*10)/100
      
   else:
      print("Invalid choice")
      return None
   return s
p=int(input("Enter the principle amount:"))
n=int(input("Enter the no of years:"))
ch=int(input("Enter 1 if you are a senior citizen else enter 2:"))
si=interest(p,n,ch)
print("Simple interest is",si)

