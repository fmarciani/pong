
# PASTE AND RUN THE FOLLOWING CODE IN HTTP://WWW.CODESKULPTOR.ORG
 
# Implementation of classic arcade game Pong
# Paste the following code into CodeSkulptor.org and run it
 
import simplegui
import random
 
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
 
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
     
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60.0, -(random.randrange(60, 180)) / 60.0]
    elif direction == LEFT:
        ball_vel = [-(random.randrange(120, 240)) / 60.0, -(random.randrange(60, 180)) / 60.0]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
     
    # defines scores
    score1 = int(0)
    score2 = int(0)
     
    # defines paddle position variables
    paddle1_pos = (HEIGHT / 2) 
    paddle2_pos = (HEIGHT / 2) 
     
    # defines paddle velocity variables
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(RIGHT)
 
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
     
    # ball collides with and bounces off of top and bottom walls
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
         
    # tests whether ball collides with left and right gutters or with paddles
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <=  paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
             
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
         
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
             
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
     
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
     
    if paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
        paddle1_vel = 0
    elif paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        paddle1_vel = 0
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
        paddle2_vel = 0
    elif paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        paddle2_vel = 0
     
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([(WIDTH - HALF_PAD_WIDTH), paddle2_pos - HALF_PAD_HEIGHT], [(WIDTH - HALF_PAD_WIDTH), paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
     
    # draw scores
    canvas.draw_text(str(score1), (200, 80), 50, "White")
    canvas.draw_text(str(score2), (375, 80), 50, "White")
         
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -4
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
 
def restart_handler():
    new_game()
 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
restart_button = frame.add_button("Restart", restart_handler, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
 
# start frame
new_game()
frame.start()
