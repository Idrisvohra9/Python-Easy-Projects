import pygame as pg
pg.init() # Initialize a few things in pygame

WIDTH, HEIGHT = 700, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ping-pong")
PI=3.14
FPS = 60
# Colors:
WHITE_Shade=(170,163,163)
DARK_Shade=(36,34,34)
ORANGE_RED=(255,69,0)
GOLD=(255,215,0)

# paddle info:
padheight, padwidth =100,20

# Class of making paddles:
class Paddle:
    color = DARK_Shade
    radius = 20
    speed = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Draw(self, win):
        pg.draw.rect(win,self.color,(self.x, self.y, self.width, self.height),border_radius=self.radius)

    def move(self,up=None):
        if up:
            self.y -= self.speed
        else:
            self.y += self.speed

class Ball:
    max_speed = 5
    color = ORANGE_RED
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_speed = self.max_speed
        self.y_speed = 0

    def Draw(self,win):
        pg.draw.circle(win,self.color,(self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

# This function contains all the elements of the game such as ping-pong paddle, background color, ball
def Elements(win, lpaddle, rpaddle, ball):
    win.fill(WHITE_Shade) # Filling The background color

# Drawing both the paddles
    lpaddle.Draw(win)
    rpaddle.Draw(win)
    for i in range(10, HEIGHT-10):
        pg.draw.arc(WIN,GOLD,[247,97,200,300], PI/2, PI, 10)
        pg.draw.arc(WIN,GOLD,[247,97,200,300], 3*PI/2, 2*PI, 10)
        break
    ball.Draw(WIN)
    
    pg.display.update() # This will update the background color changing operation

def handle_pad_moves(keys, left_paddle, right_paddle):
    # Player 1 Controls:
    if keys[pg.K_w] and left_paddle.y - left_paddle.speed >=0: # Upper limit
        left_paddle.move(up=True)

    elif keys[pg.K_s] and left_paddle.y + left_paddle.speed + left_paddle.height <= HEIGHT: # Lower limit
        left_paddle.move(up=False)

    # Player 2 Controls:
    if keys[pg.K_UP] and right_paddle.y - right_paddle.speed >=0: # Upper limit
        right_paddle.move(up=True)

    elif keys[pg.K_DOWN] and right_paddle.y + right_paddle.speed + right_paddle.height <= HEIGHT: # Lower limit
        right_paddle.move(up=False)

def handle_collision(ball, left_paddle, right_paddle):
    # Border collision:
    if ball.y - ball.radius <= 0: # Ceiling collision
        ball.y_speed *= -1 # if collide then reverse the Direction

    elif ball.y + ball.radius >= HEIGHT: # Floor collision 
        ball.y_speed *= -1

    if ball.x_speed < 0: # If the ball collides directly in middle
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_speed *= -1
        
                middle_y = left_paddle.y - left_paddle.height // 2
                difference_in_y =   middle_y - ball.y

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_speed *= -1

# This function makes sure the running of the game
def main():
    run= True
    clock = pg.time.Clock() # This allows the game to run at the same speed in every device
    left_paddle= Paddle(10, HEIGHT//2 - padheight//2, padwidth, padheight) # height of the paddle= 100, width=20, we are positioning the paddle on the y axis so that it is exactly in the middle of the left side

    right_paddle= Paddle(WIDTH- 10 - padwidth, HEIGHT//2 - padheight//2, padwidth, padheight) #We are positioning this paddle on the y axis such that it is exactly in the middle of the Right side and the opposite of the left paddle
    ball= Ball(WIDTH//2,HEIGHT//2,10)

    while run:
        clock.tick(FPS) # This means that the game will run at 60 FPS
        Elements(WIN, left_paddle, right_paddle, ball)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run= False

        keys = pg.key.get_pressed()
        handle_pad_moves(keys, left_paddle, right_paddle)
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)
    pg.quit()

if __name__ == "__main__": # This is just so the game runs in this program only and not if it is imported to other file.
    main()