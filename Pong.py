# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
position1 = [150, 100]
position2 = [450, 100]
sec = 60.0
# Constant for random velocity generation
VSCALE = 2
VOFFSETX = 2
VOFFSETY = 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(RIGHT):
    global ball_pos, ball_vel # these are vectors stored as lists
    global sec

    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [VOFFSETX, VOFFSETY]
#   if direction:
    if RIGHT:
        dir = 1
    else:
        dir = -1
    ball_vel[0] = random.randrange(120, 240)/sec*dir
    ball_vel[1] = random.randrange(60, 180)/sec*(-1.0)
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global RIGHT
    score1 = 0
    score2 = 0
    
    spawn_ball(RIGHT)
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2    
    paddle1_vel = 0
    paddle2_vel = 0

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    global ball_pos
    global RIGHT

    paddle1_bodu = paddle1_pos - HALF_PAD_HEIGHT 
    paddle1_bodd = paddle1_pos + HALF_PAD_HEIGHT
    paddle2_bodu = paddle2_pos - HALF_PAD_HEIGHT
    paddle2_bodd = paddle2_pos + HALF_PAD_HEIGHT  
    
#    new_game()
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
#    print ball_vel[0]
#    print (ball_pos[0] + BALL_RADIUS)
#    print ball_pos[1] + BALL_RADIUS >= HEIGHT
    if (ball_vel[1]>0) and (ball_pos[1] + BALL_RADIUS >= HEIGHT):
        ball_vel[1] = ball_vel[1]*(-1)  
    if (ball_vel[1]<0) and (ball_pos[1] - BALL_RADIUS <= 0):
        ball_vel[1] = ball_vel[1]*(-1)
    if ((ball_vel[0]<0) and (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH )
    and not(ball_pos[1]>paddle1_bodu and ball_pos[1]<paddle1_bodd)): 
        spawn_ball(True)
    if ((ball_vel[0]<0) and (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH )
    and (ball_pos[1]>paddle1_bodu and ball_pos[1]<paddle1_bodd)): 
        ball_vel[0] = ball_vel[0]*(-1)
    if ((ball_vel[0]>0) and (ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH ) 
    and not (ball_pos[1]>paddle2_bodu and ball_pos[1]<paddle2_bodd)):
        spawn_ball(LEFT)
    if ((ball_vel[0]>0) and (ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH ) 
    and (ball_pos[1]>paddle2_bodu and ball_pos[1]<paddle2_bodd)):
        ball_vel[0] = ball_vel[0]*(-1)


    ball_pos[0] = ball_pos[0] + ball_vel[0] 
    ball_pos[1] = ball_pos[1] + ball_vel[1]         
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")   
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_vel>0) and (paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel < HEIGHT):
      paddle1_pos = paddle1_pos + paddle1_vel
    if (paddle1_vel<0) and (paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel > 0 ):
      paddle1_pos = paddle1_pos + paddle1_vel
    if (paddle2_vel>0) and (paddle2_pos + HALF_PAD_HEIGHT + paddle1_vel< HEIGHT):
      paddle2_pos = paddle2_pos + paddle2_vel
    if (paddle2_vel<0) and (paddle2_pos - HALF_PAD_HEIGHT +paddle1_vel > 0 ): 
      paddle2_pos = paddle2_pos + paddle2_vel                

    # draw paddles        
    canvas.draw_polygon([[0, paddle1_bodu], 
                         [8, paddle1_bodu], 
                         [8, paddle1_bodd],
                         [0, paddle1_bodd]],
                         1, 'White', 'White') 
    canvas.draw_polygon([[592, paddle2_bodu], 
                         [600, paddle2_bodu], 
                         [600, paddle2_bodd],
                         [592, paddle2_bodd]],
                         1, 'White', 'White')      

    # determine whether paddle and ball collide    
    if ( not(ball_pos[1]>paddle1_bodu and ball_pos[1]<paddle1_bodd) and (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH)):
        score2 = score2 + 1
    if ( (ball_pos[1]>paddle1_bodu and ball_pos[1]<paddle1_bodd) and (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH)):
        ball_vel[0] = ball_vel[0] * 1.10
        ball_vel[1] = ball_vel[1] * 1.10
    if ( not(ball_pos[1]>paddle2_bodu and ball_pos[1]<paddle2_bodd) and (ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH)):
        score1 = score1 + 1
    if ( (ball_pos[1]>paddle2_bodu and ball_pos[1]<paddle2_bodd) and (ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH)):
        ball_vel[0] = ball_vel[0] * 1.10
        ball_vel[1] = ball_vel[1] * 1.10
        
    # draw scores
    canvas.draw_text(str(score1), position1, 36, "white")
    canvas.draw_text(str(score2), position2, 36, "white")

def keydown(key):
    global RIGHT
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
def restart_handler():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_handler, 200)

# start frame
new_game()
frame.start()
