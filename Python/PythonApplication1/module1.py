#coding:utf-8
array=[12,'klkjl',6,'cas',12.9966]
for index,a in enumerate(array):
    print(index,a)
    c=1
print("kok"if c==1 else"230")
print('''\n\n
\n
\n
\n''')
for i in range(5):
 print(i)
counter = 10
print('\n\n')
while counter > 0:
 counter=counter-1
 if (counter%3)!=0:
    continue
 print(counter)
print('''\n\n
\n
\n
\n''')
try:
 answer=12/0;
 print(answer)
except:
 print("error!")
try:
 userInput1=int(input("please input a number:"))
 userInput2=int(input("Please input another number:"))
 answer=userInput1/userInput2
 print("the answer is ",answer)
 myFile=open("missing.txt",'rw')
except ValueError:
 print("Error:You did not input a number")
except ZeroDivisionError:
 print("Error:cannot divided by 0")
except Exception as e:
 print("Unknown error: ",e)
x=2
y=3
import prime
prime.ex(x,y)
f=open("missing.txt","r") 
firstline=f.readline()
secondline=f.readline()
print(firstline,end='')
print(secondline,end='')
for line in f:
  print(line,end=' ')
f.close()
f=open("missing.txt","a")
f.write('\nThis will be appended.')
f.write('\npython is fun!')
f.close()

inputFile=open('myfile.txt','r')
outputFile=open('myoutputFile.txt','w')
msg=inputFile.read(10)

while (len(msg)!=0):
    outputFile.write(msg)
    msg=inputFile.read(10)
inputFile.close()
outputFile.close()

inputFile=open('myfile.jpg','rb')
outputFile=open('myoutputFile.jpg','wb')
msg=inputFile.read(10)

while (len(msg)!=0):#display
    #中文
    outputFile.write(msg)
    msg=inputFile.read(10)
inputFile.close()
outputFile.close()
print("\n")

for  i in range(10):
    print(i)
    print(i)
    print(i)
a=1
b="123"
print(a)
print(b)
a=b
print(a)
print(not 1)
i=1
j=i
print(j is not i)
a=1
b=3
print(a,b)
if a<b:
    a,b=b,a;
print(a,b)
if 1<a<4:
    print(a)
if 1<a>2:
    print(a)
for j in range(1,10):
    for i in range(1,j+1):
        print(j,"*",i,"=",i*j,'\t',end='')
    print("")