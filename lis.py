n=[1,2,3,4,5,6,7,8]
key=int(input("Enter the key:"))
b=0
for i in n:
    if b==key:
      break
    else:
      p=n.pop()
      n.append(p)
      b+=1
      print(b)
print(n)      

