from tkinter.messagebox import *
from math import*
import winsound
from sys import exit
from Ball import*
from  Bat import*

colors=['green', 'blue', 'yellow', 'red', 'orange', 'white', 'gray', 'navy', 'pink', 'crimson', ]


try:
    max_score=int(open("max_score", "r").read())
except:
    open("max_score", "w").close()
    max_score = 0

def hit_horn(ball,x,y):
    x=sqrt(pow(ball.x-x,2)+pow(ball.y-y,2))
    ex=x-ball.x
    ey=y-ball.y
    e=sqrt(ex*ex+ey*ey)
    ex=ex/e
    ey=ey/e
    v=sqrt(ball.x*ball.x+ball.y*ball.y)
    cosa=((x-ball.x)*ball.vx+(y-ball.y)*ball.vy)/(x*v)
    if x<=ball.r and cosa>0 and x>ball.r+7:
        len_e=2*cosa*v
        ball.vx=ex*len_e+ball.vx
        ball.vy=ey*len_e+ball.vy


def hit_object(ball,object):
    #left
    if ball.x+ball.r>=object.x and \
        ball.x+ball.r<=object.x+10 and \
        ball.y>=object.y and \
         ball.y<=object.y+object.height and \
          ball.vx>0:
        ball.turn_x()
        return 1
    #up
    if ball.x>=object.x and \
        ball.x<=object.x+object.long and \
         ball.y+ball.r>=object.y and \
          ball.y+ball.r<=object.y+20 and \
          ball.vy>0:
        ball.turn_y()
        return 1
    #right
    if ball.x-ball.r<=object.long+object.x and \
        ball.x-ball.r>=object.long+object.x-10 and \
        ball.y>=object.y and \
         ball.y<=object.y+object.height and \
          ball.vx<0:
        ball.turn_x()
        return 1
    #down
    if ball.x>=object.x and \
        ball.x<=object.x+object.long and \
         ball.y-ball.r<=object.y+object.height and \
          ball.y-ball.r>=object.y+object.height -10 and \
           ball.vy<0:
        ball.turn_y()
        return 1
    #left_up
    hit_horn(ball,object.x,object.y)
    #right_up
    hit_horn(ball,object.x+object.long,object.y)
    #left_down
    hit_horn(ball,object.x,object.y+object.height)
    #right_down
    hit_horn(ball,object.x+object.long,object.y+object.height)

def hit_wall(ball,object,canvas_width,score):
    if ball.x-ball.r<=0 and ball.vx<0:
        ball.turn_x()
        return 1
    if ball.x+ball.r>=canvas_width and ball.vx>0:
        ball.turn_x()
        return 1
    if ball.y-ball.r<=0 and ball.vy<0:
        ball.turn_y()
        return 1
    if ball.y+ball.r>=object.y+object.height+15 and ball.vy>0:
        if score > max_score:
            showwarning("Warning!", "Game Over!!!\nscore: " + str(score) + str('\nBest Score!'))
            open("max_score", "w").write(str(score))
        else:
            winsound.PlaySound(r"./fail.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            showwarning("Warning!", "Game Over!!!\nscore: " + str(score))
        return 0
