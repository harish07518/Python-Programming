def prime(n):
   if(n==2):
      return 1
   else:
      for i in range(2,n):
	 if(n%i==0):
	    flag=1
	    break
	 flag=0
      if (flag==1):
	 return 0
      else:
	 return 1
x=int(input("Enter a number:"))
ans=prime(x)
if ans==1:
   print("Prime number")
else:
   print("Not a Prime number")
