# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

num_range = 100
secret_number = 0
guesses = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_number 
    global guesses

    secret_number = random.randrange(0, num_range)
    
    if num_range == 100:
        guesses = 5
    elif num_range == 1000:
        guesses = 10
    
    print "New game. The range is from 0 to", num_range, "."
    print "Number of remaining guesses: ", guesses
    
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses
    global secret_number
    
    won = False
    
    print "Your guess was ", guess
    guesses = guesses - 1
    print "Number of remaining guesses: ", guesses
    
    if int(guess) == secret_number:
        won = True
    elif int(guess) > secret_number:
        result = "Lower!!"
    else: 
        result = "Higher!!"
   
    if won: 
        print "You got the answer!!"
        new_game()
        return 
    elif guesses == 0:
        print "Game Over !!"
        new_game()
    else: 
        print result
        

    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

#create control elements 
button1 = frame.add_button("Range is [0,100)", range100, 200)
button2 = frame.add_button("Range is [0, 1000)", range1000, 200)
input_field = frame.add_input("My input", input_guess, 50)

frame.start()

# call new_game 
new_game()


