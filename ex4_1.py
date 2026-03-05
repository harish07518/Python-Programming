def max_num(a,b,c):
   if(a>b and a>c):
      return a
   elif(b>c and b>a):
      return b
   else:
      return c
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
print("The largest number is "+ str(max_num(x,y,z)))

