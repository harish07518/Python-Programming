print("Interest calculation\nPress'1' to calculate simple interst\nPress'2' to calculate compound interest")
ch = int(input())
p = float(input("\nEnter the principle amount:"))
n = float(input("\nEnter the periodof year:"))
r =float(input("\nEnter the rate of interest:"))
if(ch==1):
   ans=(p*n*r)/100
   print("Simple Interest:"+str(ans))
elif(ch==2):
   t= float(input("Enter the compunding time period:"))
   ans = p*((1+((r*n)/100))**(n*t))
   ans=ans-p
   print("Compound Interest:"+str(ans))
else:
   print("Enter a valid choice")
