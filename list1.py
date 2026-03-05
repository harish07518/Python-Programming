#a=[9,8,7,9,8,6,4]
#sum=0
#for i in a:
 #  sum+=i
#print("SUM of A =",sum,"\nMEAN of A =",sum//7)
#b=(input("Enter the elements in list:")).split()
#print(b)
c=list(map(int,input("Enter the elements in list:").split()))
print(c)
sum1=0
for i in c:
   sum1+=i
print("SUM of C =",sum1,"\nMEAN of C =",sum1//(len(c)))
