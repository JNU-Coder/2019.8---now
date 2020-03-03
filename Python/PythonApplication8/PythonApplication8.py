f=open("G://Python//PythonApplication8//1.txt",'r+')
x=['\n','klk\nsk\ndh\nks','ui\nhi','\nsjd\nl\ns\n\n\n\nd']
f.write('233555\n6564')
f.writelines(x)
for i in f:
    print(i,end='')    
f.close()