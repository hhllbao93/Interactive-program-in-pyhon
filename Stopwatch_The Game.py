# "Stopwatch: The Game"
import simplegui
counter = 0
cor_guess = 0
tot_guess = 0
time_form = "0:00.0"
running = False

# define global variables
position1 = [100, 150]
position2 = [200, 50]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(val):
   val1 = val
   A = val1//600
   val1 = val1/10
   B = (val1%60)//10
   C = (val1%60)%10
   D = val%10
   return str(A)+":"+str(B)+str(C)+"."+str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    running = True
    timer.start()

def stop_handler():
    global cor_guess, tot_guess, running
#    print running
    if running == True:
      if (counter%10==0):
        cor_guess = cor_guess+1
      tot_guess = tot_guess+1
    running = False
    timer.stop()
    
def reset_handler():
    global counter, cor_guess, tot_guess
    counter = 0
    cor_guess = 0
    tot_guess = 0
    timer.stop()
    global time_form
    time_form = format(counter)

def timer_handler():
    """reset timer"""
    global counter
    counter = counter + 1
    global time_form
    time_form = format(counter)
    print time_form
    
# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), position1, 36, "white")
    canvas.draw_text(str(cor_guess)+'/'+str(tot_guess), position2, 30, "red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
frame.add_button("Start", start_handler,150)
frame.add_button("Stop", stop_handler,150)
frame.add_button("Reset", reset_handler,150)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
