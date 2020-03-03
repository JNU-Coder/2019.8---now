import turtle as t
t.title('自动轨迹绘制')
t.setup(1920,1080,0,0)
t.penup()
t.pencolor('red')
t.pensize(5)
t.backward(500)
t.write('自动轨迹绘制:',font=("",20,"normal"))
t.fd(500)
data=[]
f=open('1.txt')
for i in f:
    i=i.replace('\n','')
    data.append(list(map(eval,i.split(','))))
t.pendown()
for i in range(len(data)):
    t.pencolor(data[i][3],data[i][4],data[i][5])
    t.fd(data[i][0])
    if data[i][1]:
        t.right(data[i][2])
    else:
        t.left(data[i][2])
t.done()
