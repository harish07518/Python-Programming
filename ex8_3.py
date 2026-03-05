num1=set()
num2=set()
n1=int(input("Enter the no.of elements in set1:"))
n2=int(input("Enter the no.of elements in set2:"))
for i in range(n1):
   num1.add(input("Enter value:"))
for i in range(n2):
   num2.add(input("Enter value:"))
print("Set1:",num1)
print("Set2:",num2)
print("Union:",num1.union(num2))
print("Intersection:",num1.intersection(num2))
print("Diffrence:",num1.difference(num2))

