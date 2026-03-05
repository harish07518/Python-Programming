a=int(input("Enter the hour timing of entry:"))
b=int(input("Enter the minute timing of entry:"))
c=int(input("Enter the hour timing of leaving:"))
d=int(input("Enter the minute timing of leaving:"))
veh=input("Enter the vehicle type:")
x=c-a
y=d-b
z=(x*60)+y
hr=z//60
mi=z%60
print("The total hours parked by the vehicle is",hr,"hours",mi,"minutes")
if veh=='truck' or veh=='bus' :
   if z>=180 :
      print("The cost of parking is 30rs")
   else :
      print("The cost of parking is 20rs")
elif veh=='car' or veh=='auto':
   if z>=180 :
      print("The cost of parking is 20rs")
   else:
      print("The cost of parking is 10rs")
elif veh=='cycle' or veh=='motorcycle' or veh=='scooter' :
   if z>=180 :
      print("The cost of parking is 10rs")
   else :
      print("The cost of parking is 5rs")
else:
   print("invalid vehicle details")


