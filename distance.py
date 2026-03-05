x1=float(input("Enter x1 coordinate:"))
x2=float(input("Enter x2 coordinate:")) 
y1=float(input("Enter y1 coordinate:"))
y2=float(input("Enter y2 coordinate:"))
d=((((x2 - x1) ** 2) + ((y2 - y1) ** 2))) ** 0.5
print("The distance between coordinates ({0},{1}) and ({2},{3}) is {4:.4f}".format(x1,y1,x2,y2,d))
