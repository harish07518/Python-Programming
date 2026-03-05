a=float(input("Enter the coefficient of square term:"))
b=float(input("\nEnter the coefficient b:"))
c=float(input("\nEnter the constant term:"))
det = (b**2) - (4*a*c)
if (det>0):
   ans1 = ((-b + (det**0.5))/(2*a))
   ans2 = ((-b - (det**0.5))/(2*a))
   print("\nThe Quadratic roots are:"+str(ans1)+"\t"+str(ans2))
elif (det == 0):
   ans1 = (-b/(2*a))
   print ("\nThe Quadratic roots are:"+str(ans1)+"\t"+str(ans1))
else:
   det=-det
   ans_real = (-b/(2*a))
   ans_img = (det**0.5)/(2*a)
   print("The Quadratic roots are:"+ans_real+"+j"+ans_img+"\t"+ans_real+"-j"+ans_img)

