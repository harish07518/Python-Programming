n=int(input("Enter a number:"))
arm=0
temp=n
while(temp!=0):
   r=temp%10
   arm=arm+(r**3)
   temp=temp//10
if arm==n:
   print("Armstrong number")
else:
   print("not a armstrong number")
