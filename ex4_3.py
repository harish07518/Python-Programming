def swap(a,b):
   a=a+b
   b=a-b
   a=a-b
   print("After swapping the numbers are "+str(a)+","+str(b))
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("Before swapping the numbers are "+str(a)+","+str(b))
swap(a,b)
