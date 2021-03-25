number = int(input("Enter the number to be tested odd or even"))
num = int(input("Enter the dividend"))
if(number%2==0):
  print("The number is even")
else:
    print("The number is odd")
if(number%4==0):
  print(f"Hurray {number} is a multiple of 4")
if(number%num==0):
  print(f"Yayy {number} is evenly divided by {num}")
else:
  print(f" {number} cannot be divided by {num}")