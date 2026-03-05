p=int(input("Enter the amount of purchase:"))
i=int(input("Enter the amount given by the customer:"))
rem=i-p
a=1
if rem!=0 and rem>0:
  n5=rem/500
  n5r=rem%500
  print("Give {} 500rs notes".format(n5))
  if n5r==0:
   break
  elif a==1:
     if n5!=0:
      n2=n5r/200
      n2r=n5r%200
      print("Give {} 200s notes".format(n2))
     elif n5==0:
      n2=rem/200
      n2r=rem%200
      print("Give {} 200rs notes".format(n2))
     else: 
        break
  elif a==1:
       if n2!=0:
        n1=n2r/100
        n1r=n2r%100
        print("Give {} 100rs notes".format(n1))
       elif n2==0:
	 n1=n5r/100
	 n1r=n5r%100
	 print("give {} 100rs notes".format(n1))
       else: 
         break
  elif a==1:
          n50=n1r/50
          n50r=n1r%50
          print("give {} 50rs notes".format(n50))
          break
else:
 print("Invlid transtion")
  
