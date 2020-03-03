def f(n):
    if n==0:
        return 1
    return n*f(n-1)
print(f(1))
s='12345'
s=s[::-1]
print(s)
def reverse(s):
    if s=='':
        return s
    else:
        return reverse(s[1:])+s[0]
print(reverse(s))
def fb(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
print(fb(3))
count=0
def han(n,left,right,mid):
    global count
    if n==1:
        print('{}:{}->{}'.format(1,left,right))
        count+=1
    else:
        han(n-1,left,mid,right)
        print("{}:{}->{}".format(n,left,right))
        count+=1
        han(n-1,mid,right,left)
a='a'
b='b'
c='c'
m=han(4,a,c,b)
print(count)
import turtle
turtle.setup(1920,1080,0,0)
turtle.speed(100000)
turtle.penup()
turtle.backward(500)
turtle.pendown()
def k(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            k(size/3,n-1)
for i in range(3):
    k(300,6)
    turtle.right(120)
turtle.done()