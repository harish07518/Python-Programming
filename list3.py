a=list(map(int,input("Enter the elements of list:").split()))
print("The elements in the list are:",a)
elt=int(input("The element to be searched is:"))
ind=[]
for index,value in enumerate(a):
   if value == elt:
      ind.append(index)
print("The no.of the times the element found is:",len(ind),"\nThe element is found in the indices:",ind)
