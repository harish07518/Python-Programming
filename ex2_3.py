num=int(input("Enter a number:"))
sum1=0
temp = num
while(num!=0):
      n=num%10
      sum1=sum1+(n*n*n)
      num=num/10
if(temp == sum1):
   print(" Is a armstrong number")
else:
   print(" Is not a armstrong number")

