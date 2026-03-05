l1=[i for i in input("enter space separated elements:").split()]
l2=[]
for i in l1:
   if i not in l2:
      l2.append(i)
x=set(l2)
print("set:",x)
def add(x):
   a=input("enter a value:")
   if a in x:
      print("element already exist!!")
   else:
      x.add(a)
add(x)
add(x)
print("set after adding:",x)
def remove(x):
   b=input("enter  a value:")
   if b in x:
      x.remove(b)
   else:
      print("elemnt doesnot exist!!")
remove(x)
remove(x)
print("set after removing:",x)
 
