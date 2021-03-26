decision = 'Y'
while(decision == 'Y' or decision == 'y' ):
 player1 = input("Player1 : Rock/Paper/Scissors ") 
 player2 = input("Player 2 :Rock/Paper/Scissors ")
 if(player1!="" and player2!=""): 
    if((player1.lower()=="rock" or player1.lower()=="paper" or player1.lower()=="scissors") and(player2.lower()=="rock" or player2.lower()=="paper" or player2.lower()=="scissors")):
       if(player1.lower()==player2.lower()):
         print("Both played same hence No winner")
       elif((player1.lower() == "rock" and player2.lower() == "scissors") or (player1.lower() == "paper" and player2.lower() == "rock") or (player1.lower()=="scissors" and player2.lower()=="paper")):
         print("player1 wins")
       else: 
         print("player2 wins")
    else:
        print("Invalid Input. Please choose between Rock/Paper/Scissors only")
    decision = input("Do you want to continue the game? Press Y/N ")
  

   

 


