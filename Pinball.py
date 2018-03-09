from tkinter import*
from Ball import *
from Bat import *
import Physics
import time
import random
from tkinter.messagebox import*
import winsound
import threading
import os

colors=['green', 'blue', 'yellow', 'red', 'orange', 'white', 'gray', 'navy', 'pink', 'crimson', ]

score=0
level=1
flag=0

background_color=random.sample(colors,1)
ball_color=random.sample(colors,1)
paddle_color=random.sample(colors,1)
while(ball_color==background_color):
    ball_color = random.sample(colors, 1)
while(paddle_color==background_color):
    paddle_color = random.sample(colors, 1)

try:
    max_score=int(open("max_score", "r").read())
except:
    open("max_score", "w").close()
    max_score = 0

tk = Tk()
tk.title("pinball")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=800, height=600, bd=0,bg=background_color, highlightthickness=0)
canvas.pack()
tk.update()
canvas_height = canvas.winfo_height()
canvas_width=canvas.winfo_width()

paddle = Paddle(canvas, paddle_color, random.uniform(0, canvas_width - 100), canvas_height - 50, 100, 20)
x_original = paddle.x + paddle.long / 2
y_original = paddle.y - 10
ball = Ball(canvas, ball_color, x_original, y_original, 10)

bar = Bar(canvas, random.sample(colors, 1), random.uniform(0, canvas_width), random.uniform(0, 200),
                  random.uniform(0, canvas_width), random.uniform(0, 200))
bar.reset()
bar1 = Bar(canvas, background_color, 0, 0, 66, 164)

def draw_text(canvas):
    global score,level
    canvas.delete("score",'level','speed')
    canvas.create_text(canvas_width - 100, 50, text="SCORE:  " + str(score),tag="score")
    canvas.create_text(canvas_width - 100, 30, text="LEVEL:  " + str(level),tag='level')
    canvas.create_text(canvas_width - 100, 70, text="SPEED:  " + str(paddle.speed),tag='speed')
    canvas.create_text(canvas_width - 100, 90, text="Best Score:  " + str(max_score), tag='score')

def pinball():

    global score,level,flag,max_score
    while(True):
        if flag%2==0:
            paddle.move()
            ball.move()
        if Physics.hit_object(ball,bar):
            if ball.color==bar.color:
                score+=3
        Physics.hit_object(ball,bar1)
        if Physics.hit_wall(ball,paddle,canvas_width,score)==1:
            score+=1
        if Physics.hit_wall(ball, paddle, canvas_width, score) == 0:
            canvas.delete(ball.id,paddle.id,bar.id)
            paddle.id = paddle.canvas.create_rectangle(paddle.pos, fill=paddle.color)
            x_original = paddle.x + paddle.long / 2
            y_original = paddle.y - 10
            ball.id = ball.canvas.create_oval(x_original-ball.r, y_original - ball.r, x_original + ball.r, y_original + ball.r, fill=ball.color)
            bar.reset()
            score=0
            max_score = int(open("max_score", "r").read())
            level=1
            break
        draw_text(canvas)
        if Physics.hit_object(ball,paddle):
            canvas.delete(ball.id)
            ball.color = random.sample(colors, 1)
            while (ball.color == background_color):
                ball.color = random.sample(colors, 1)
            ball.id = ball.canvas.create_oval(ball.pos, fill=ball.color)
            if (ball.color == paddle_color):
                score += 10
            else:
                score += 5
        if score >= level * 40:
            level += 1
            ball.speed += 1
            paddle.long -= 5
            bar.reset()
            canvas.delete(paddle.id)
            paddle.color = random.sample(colors, 1)
            while (paddle.color == background_color):
                paddle.color = random.sample(colors, 1)
            paddle.id = paddle.canvas.create_rectangle(paddle.pos, fill=paddle.color)
            canvas.delete(paddle.id)
            paddle.color = random.sample(colors, 1)
            while (paddle.color == background_color):
                paddle.color = random.sample(colors, 1)
            paddle.id = paddle.canvas.create_rectangle(paddle.pos, fill=paddle.color)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

def playmusic():
    music=random.sample(os.listdir("./music"),1)[0]
    winsound.PlaySound('./music/'+music, winsound.SND_FILENAME | winsound.SND_ASYNC)

t1=threading.Thread(target=playmusic,name='playmusic')
t1.start()
t1.join()

#showinfo('Introduce','Welcome to PinBall Game!\n                              Chaf Chen')
def pause():
    global flag
    flag+=1
    if(flag%2==0):
        button3['text']='Pause'
    else:
        button3['text']='Continue'
def Quit():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Goodbye!')
        tk.destroy()
    else:
        showinfo('No', 'Quit has been cancelled!')
def rule():
    showinfo("rule","Don't let the ball fell and try to hit the wall \
and the paddle as many times as possible.\
Hit the paddle,you will get 5 points.The color of the ball and the paddle \
can change.When the ball and the paddle have the same color,you will get \
10 points if you can catch the ball.Don't worry,you still can get 1 point \
when the ball hit the wall.Have fun!"
                    )
button1=Button(tk,text="Start",width=9,height=2,command=pinball)
button2=Button(tk,text="Rule",width=9,height=2,command=rule)
button3=Button(tk,text='Pause',width=9,height=2,command=pause)
button4=Button(tk,text="Quit",width=9,height=2,command=Quit)

id1=canvas.create_window(30,20,window=button1)
id2=canvas.create_window(30,60,window=button2)
id3=canvas.create_window(30,100,window=button3)
id4=canvas.create_window(30,140,window=button4)

tk.iconbitmap('./launcher.ico')
tk.mainloop()
