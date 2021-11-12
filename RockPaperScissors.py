from random import randint

#Ask user for their name, it will be later displayed if they win saying "Congrats (Entered name). You win!" There is no loop so it will only ask on the initial run
firstName = input("Hello! What is your name? \n")
print("Hello " + firstName + "!\n")



# Set the possibilities of the computer to pick randomly
y = ["Rock", "Paper", "Scissors"]

#Setting the computer to pick a random integer from the index range of 0 - 2
computer = y[randint(0,2)]

#Set the player to the boolean of False
player = False

#While the player is False, run the below code of asking the player for an input and following the if statement depending what the player selects, and the computer randomly selects
while player == False:

    #Ask the player for the exact input of Rock, Paper, or Scissors (Case sensitive)
    player = input("Rock, Paper, Scissors? ")

    #If the player and computer has the same selection, output that the game was a tie
    if player == computer:
        print("TIE!\n")


        #elif statement to run through the possibilites of IF the player selects an option, AND the computer selects the option, to display the appropriate outcome
    elif player == "Rock":
         if computer == "Paper":
             print("Paper covers rock, " + "Computer wins with picking " + computer + '\n')

         if computer == "Scissors":
             print("Rock breaks " + computer + ". Congrats "+ firstName + ", You Win!\n") 

    elif player == "Scissors":
        if computer == "Rock":
            print("Rock Breaks scissors, "  + "Computer wins with picking " + computer + '\n') 

        if computer == "Paper":
            print("Scissors cuts " + computer + ". Congrats " + firstName + ", You Win!\n") 

    elif player == "Paper":
        if computer == "Scissors":
            print("Scissors cuts paper, "  + "Computer wins with picking " + computer + '\n')

        if computer == "Rock":
            print("Paper covers " + computer + ". Congrats " + firstName + ", You Win!\n")


    #Else nothing was selected from the above elif statement, output the below statement
    else:
        print("Error, check your spelling please!")
        
        #This loops the player once the outcome has been displayed to run the program again from the top
    player = False
    computer = y[randint(0,2)]


