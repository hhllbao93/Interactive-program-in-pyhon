# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
n = 7

# helper function to start and restart the game
def new_game():
    global num_range, n, secret_number
    if num_range == 100:
        n = 7
    elif num_range == 1000:
        n = 10
    secret_number = random.randrange(0, num_range)
    if n > 0:
        print "New game. Range is from 0 to ", num_range 
        print "Number of remaining guesses is ", n
        print "              "

# define event handlers for control panel
def range100():
    global secret_number, n, num_range
    n = 7
    num_range = 100
    secret_number = random.randrange(0, 100)
    new_game()

def range1000():
    global secret_number, n, num_range
    n = 10
    num_range = 1000
    secret_number = random.randrange(0, 1000)
    new_game()
    
def get_input(inp):
    # main game logic goes here	
    global guess,n
    guess = int(inp)
    n = n - 1
    
    print "Your guess was", guess
    print "Number of remaining guesses is ", n
    
    if n > 0:    
        if guess == secret_number:
            print "Correct!!"
            print "              "            
            new_game()
        elif guess < secret_number:
            print "Higher!!"
            print "              "
        elif guess > secret_number:
            print "Lower!!"
            print "              "
    else:
        print "Out of guesses! The number was ", secret_number
        print "              "        
        new_game()
    
# create frame
f = simplegui.create_frame("Guess number",300,300)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 100)

new_game()
f.start

# always remember to check your completed program against the grading rubric
