a=float(input("Enter the side1 of triangle:"))
b=float(input("Enter the side2 of triangle:"))
c=float(input("Enter the side3 of triangle:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle is {:.2f}".format(area))
