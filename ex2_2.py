temp =input("Enter the temperature condition:")
hum = input("\nEnter the humidity condition:")
if (temp == "warm"):
   if(hum == "humid"):
      print("\nPlay Basketball")
   elif(hum=="humid"):
      print("\nPlay Tennis")
   else:
      print("\nEnter a valid input for humidity")
elif(temp=="cold"):
   if(hum=="dry"):
      print("\nPlay Cricket")
   elif(hum=="humid"):
      print("\nGo for swimming")
   else:
      print("\nEnter a valid input for humidity")
else:
   print("\nEnter a valid input for temperature")
