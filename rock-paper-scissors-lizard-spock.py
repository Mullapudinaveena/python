# Rock-paper-scissors-lizard-Spock Game
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

# helper functions
def name_to_number(name):
    if name == 'rock':
        return 0;
    elif name == 'spock':
        return 1;
    elif name == 'paper':
        return 2;
    elif name == 'lizard':
        return 3;
    elif name == 'scissors':
        return 4;
    else: 
        return 'something wrong in input';    
   
def number_to_name(number):    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4: 
        return 'scissors'
    else:
        return 'something wrong in input'

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print '-----------------------------------------'
    
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    
	player_number = int(name_to_number(player_choice))
    #print player_number
    #print type(player_number)

    # compute random guess for comp_number using random.randrange()
    
	comp_number = random.randrange(0,5)
	#print comp_number
    #print type(comp_number)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'computer chooses ' + comp_choice
    
    # compute difference of comp_number and player_numbermodulo five
    
    difference = (player_number - comp_number) % 5
    #print type(difference)
    #print difference
  
    # use if/elif/else to determine winner, print winner message
    if difference == 1 or difference == 2:
        result = 'Player'
    elif difference == 3 or difference == 4:
        result ='Computer'
    else: 
        result = 'error'
    
	#print final message according to difference calculated
    if difference:
        print result, 'wins!'
    else: 
        print 'We have a tie!'
    
# test the code 
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



