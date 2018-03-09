import random

colors=['green', 'blue', 'yellow', 'red', 'orange', 'white', 'gray', 'navy', 'pink', 'crimson', ]

#def paddle
class Paddle:
    def __init__(self,canvas,color,x,y,long,height):
        self.canvas=canvas
        self.color=color
        self.long=long
        self.x=x
        self.y=y
        self.height=height
        self.id=self.canvas.create_rectangle(self.x,self.y,self.x+self.long,self.y+self.height,fill=color)
        self.speed=20
        self.v=0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.speed_up)
        self.canvas.bind_all('<KeyPress-Down>', self.speed_down)
    def move(self):
        self.pos = self.canvas.coords(self.id)
        self.x=self.pos[0]
        self.y=self.pos[1]
        if(self.pos[2]>=self.canvas.winfo_width() and self.v>0):
            self.v=0
            return
        if(self.pos[0]<0 and self.v<0):
            self.v=0
            return
        self.canvas.move(self.id, self.v, 0)
        self.v = 0
    def turn_left(self,event):
        self.v=-self.speed
    def turn_right(self,event):
        self.v=self.speed
    def speed_up(self,event):
        if(self.speed<100):
            self.speed+=1
    def speed_down(self,event):
        if(self.speed>1):
            self.speed-=1

#def bar
class Bar:
    def __init__(self,canvas,color,x,y,long,height):
        self.canvas=canvas
        self.color=color
        self.long=long
        self.x=x
        self.y=y
        self.height=height
        self.id=self.canvas.create_rectangle(self.x,self.y,self.x+self.long,self.y+self.height,fill=color)
    def get_pos(self):
        self.pos = self.canvas.coords(self.id)
        self.x=self.pos[0]
        self.y=self.pos[1]
    def reset(self):
        self.canvas.delete(self.id)
        self.long = random.uniform(0, 800)
        self.height = random.uniform(3, 200)
        self.x = random.uniform(0, 800)
        self.y = random.uniform(0, 200)
        self.color = random.sample(colors, 1)
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + self.long, self.y + self.height, fill=self.color)
        self.get_pos()
        if self.x+self.long>800:
            self.reset()