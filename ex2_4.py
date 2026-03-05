a,b = int(input("Enter num1:")),int(input("\nEnter num2:"))
if(a>b):
   x=a
else:
   x=b
while(True):
   if(x%a==0 and x%b==0):
      ans=x
      break
   x+=1
print("\nThe L.C.M of "+str(a)+" and "+str(b)+" is "+str(x))

