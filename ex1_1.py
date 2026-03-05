print("Area of triangle calculation\nPress'1' to give input as breadth and height\nPress'2' to give input as all sides of triangle")
ch = int(input())
if ch==1 :
   br = float(input("\nEnter the breadth:"))
   h = float(input("\nEnter the height:"))
   if (br < 0 or h <0 ):
      print("\nDimensions are entered negative, give valid input")
   else:
      area= 0.5*br*h
      print ("\nArea of triangle: "+str(area))
elif ch==2:
   a=float(input("\nEnter 1st side of triangle:"))
   b=float(input("\nEnter 2nd side of triangle:"))
   c=float(input("\nEnter 3rd side of triangle:"))
   if (a<0 or b<0 or c<0):
      print("\nDimensions are invalid , give positive input")
   else:
      s = (a+b+c)/2
      area = (s*(s-a)*(s-b)*(s-c))**0.5
      print ("\nArea of triangle:"+str(area))
else:
   print("\nEnter a valid choice!")

