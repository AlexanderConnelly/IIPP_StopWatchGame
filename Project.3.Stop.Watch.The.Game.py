# template for "Stopwatch: The Game"
import simplegui
# define global variables
time=0
formated= "Start"
true_stop= False
attempts=0
score=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global formated
    A=time//600
    B=(time//10)%60//10
    C=(time//10)%60%10
    D=(time%600)%10
    
    formated= str(A) + ":" + str(B)+str(C)+"."+str(D)
    return formated
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global true_stop
    true_stop=True
    timer.start()
    
def stop_handler():
    global score,attempts,true_stop
    
    if true_stop==True and time%10==0:
        score+=1
    if true_stop==True:
        attempts+=1
        true_stop=False
    timer.stop()   
    
def reset_handler():
    global time,score,attempts
    time=0
    score=0
    attempts=0
    format(time)
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time= time+1
    format(time)


# define draw handler
def draw_handler(canvas):
    global formated,score,attempts
    canvas.draw_text(formated,(20,150),100,"Blue")
    canvas.draw_text(str(score)+"/"+str(attempts),(20,80),100,"Red")
    
# create frame
frame = simplegui.create_frame("Stop Watch: The Game", 300, 150)


# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)
start_button=frame.add_button("Start",start_handler,200)
stop_button=frame.add_button("Stop", stop_handler,200)
reset_button=frame.add_button("Reset", reset_handler,200)


# start frame
frame.start()


# Please remember to review the grading rubric
