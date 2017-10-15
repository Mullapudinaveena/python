# StopWatch - "The Game"

import simplegui

# define global variables
count = 0
interval = 1000
total = 0
success = 0
stop = True


# define helper function format  that converts integer counting tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_sec  = (t) % 10
    sec 	   = int(t / 10) % 10
    minutes    = int(t / 600) % 600
    ten_min    = int(t / 100) % 6

    string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return string
    

    
# define eventhandlers: start, stop, reset
def start():
    global count, stop
    stop = False
    timer.start()

def stop():
    global total, success, stop
    if stop == False:
        if count % 10 == 0 and count != 0:
            success += 1
            total += 1
        elif count != 0:
            total += 1
        stopped = True
        timer.stop()

def reset():
    global count, success, total
    count = 0
    stop = True
    total = 0
    success = 0
    timer.stop()
    

# define eventhandlers for timerwith 0.1 sec interval
def tick():
    global count
    count += 1

#define draw handler
def draw(canvas):
    text = format(count)
    canvas.draw_text(text, (80, 125), 42, "white")
    canvas.draw_text(str(success) + '/' + str(total), (190, 30), 24, "pink")
    pass

# create frame
frame = simplegui.create_frame("StopWatch", 400, 200)

# register eventhandlers
frame.add_button("start", start, 100)
frame.add_button("stop", stop, 100)
frame.add_button("reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start timer and frame
frame.start()
timer.start()
reset()