num1=set()
num2=set()
n1=int(input("Enter no.of elements in set1:"))
n2=int(input("Emter no.of elements in set2:"))
for i in range(n1):
   num1.add(input("Enter element:"))
for i in range(n2):
   num2.add(input("Enter value:"))
print("Set1:",num1)
print("Set2:",num2)
if (num1.issubset(num2)):
   print("Set1 is subset of set2")
elif(num2.issubset(num1)):
   print("Set2 is subset of set1")
else:
   print("Neither sets are subset to eachother")
