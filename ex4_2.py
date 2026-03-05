def fact( n):
   if(n>=1):
      return n*fact(n-1)
   elif(n==0):
      return 1
x=int(input("Enter a number:"))
print(fact(x))


