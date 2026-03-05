n = int(input("Enter the no. of elements:"))
num=set()
for i in range(n):
   num.add(input("Enter the value:"))
print("Length :",len(num))
print("Elements in set:")
for i in num:
   print(i)
def check():
   ch=input("Enter the element to check in set:")
   if ch in num:
      print("Element present")
   else:
      print("Element not in set")
check()
check()
