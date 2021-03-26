import random
decision = "start"
counter =0
while(decision.lower() == "start"):
   a = random.randint(1,9)
   b=0
   number = int(input("Enter a number to try your luck "))
   print(f"The lottery number is {a}")
   counter = counter+1
   if(number<a):
    b=a-number
    if(b<=2):
     print("The num you guessed is neither too low nor too high")
    elif(b>2):
     print("The num you guessed is too low from the lottery ball")
    else:
     print("The num you guessed is neither too high from the lottery ball")
   elif(number>a):
    b=number-a
    if(b<=2):
       print("The num you guessed is neither too low nor too high")
    elif(b>=2):
      print("The number you guessed is too high from the lottery ball")
    else:
      print("The num you guessed is neither too low from the lottery ball")
   elif(number==a):
     print("You guessed the number exactly right")
   else:
     print("This is not a valid input")
   decision = input("Enter exit to stop the game or start to retry ")
if(decision.lower() == "exit"):
 print(f"The number of guesses the user has taken is {counter}")
  