# Rock-paper-scissors-lizard-Spock 


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name == "rock":
       name2number = 0
    elif name == "Spock":	
       name2number = 1
    elif name == "paper":	
       name2number = 2
    elif name == "lizard":	
       name2number = 3
    elif name == "scissors":	
       name2number = 4
    else:
       print "Wrong input"
       name2number = None
    
    return name2number

def number_to_name(number):
    if number == 0:
       number2name = "rock"
    elif number == 1:	
       number2name = "Spock"
    elif number == 2:	
       number2name = "paper"
    elif number == 3:	
       number2name = "lizard"
    elif number == 4:	
       number2name = "scissors"
    else:
        print "Wrong input"
        number2name = None
    
    return number2name

def rpsls(player_choice): 
    print "        "
    print "Player choose ", player_choice
    number_player   = name_to_number(player_choice)
    number_computer = random.randrange(0,5)
    computer_choice = number_to_name(number_computer)
    print "Computer choose ", computer_choice    
    number_diff = (number_player - number_computer)%5
    if number_diff == 0:
        print "Player and computer tie!"
    elif number_diff <= 2:
        print "Player wins!"
    elif number_diff >= 3:
        print "Computer wins!"
    else:
        return "Something was wrong with my input."
  
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


# always remember to check your completed program against the grading rubric


