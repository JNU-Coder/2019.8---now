import turtle
import time

def drawgap():
    turtle.penup()
    turtle.fd(5)

def drawline(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdight(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)  
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,8,7,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def Data(data):
    for i in data:
        if i=='-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i=='=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("yellow")
            turtle.fd(40)
        elif i=='+':
            turtle.write('日',font=("Arial",18,"normal"))
            turtle.pencolor("purple")
            turtle.fd(40)
        elif i=='!':
            turtle.write('时',font=("Arial",18,"normal"))
            turtle.pencolor("black")
            turtle.fd(40)
        elif i=='@':
            turtle.write('分',font=("Arial",18,"normal"))
            turtle.pencolor("gray")
            turtle.fd(40)
        elif i=='#':
            turtle.write('秒',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        else:
            drawdight(eval(i))

def draw():
    turtle.setup(1920,1080,0,0)
    turtle.penup()
    turtle.speed(20)
    turtle.backward(600)
    turtle.pensize(5)
    turtle.pencolor("red")
    t = time.gmtime()
    t=time.strftime("%Y-%m=%d+%H!%M@%S#",t)
    print(t)
    Data(t)
    turtle.hideturtle()
    turtle.done()

draw()


