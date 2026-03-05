n= int (input("Enter the input:"))
print("\n")
for i in range ((2*n)+1):
   if(i<=n):
      print((n-i)*" "+(i*"* "))
      
   else:
      print((i-n)*" "+(((2*n)-i)*"* "))
      

