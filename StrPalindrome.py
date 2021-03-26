name = input("Enter a String ")
reverse_Name = ""
for s in name:
 reverse_Name = s + reverse_Name
if(reverse_Name.lower() == name.lower()):
  print("The string is a palandrome")
else:
  print("The string is not a palandrome")

