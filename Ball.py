from math import*
import random

#define ball
class Ball:
    def __init__(self,canvas,color,x,y,r):
        self.canvas=canvas
        self.r=r
        self.x=x
        self.y=y
        self.color=color
        self.id=self.canvas.create_oval(x-self.r, y-self.r, x+self.r, y+self.r,fill=self.color)
        self.speed=5
        self.angle=random.sample([random.uniform(-pi/3,-pi/10),random.uniform(pi/10,pi/3)],1)[0]
        self.vx=sin(self.angle)
        self.vy=-cos(self.angle)
    def move(self):
        self.canvas.move(self.id,self.speed*self.vx,self.speed*self.vy)
        self.pos = self.canvas.coords(self.id)
        self.x=self.pos[0]+self.r
        self.y=self.pos[1]+self.r
    def turn_x(self):
        self.vx=-self.vx
    def turn_y(self):
        self.vy=-self.vy
