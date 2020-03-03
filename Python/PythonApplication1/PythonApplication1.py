import module1
import module2
import sys
import os
import time
from module2 import StudentsInfo

def sumFromScreen():
    print("please input two integer,separated by space:")
    line=sys.stdin.readline()
    num=[int(str_num) for str_num in line.split()]
    print("the sum is:%d"%(num[0]+num[1]))

def sum(*p):
    s=0
    for i in p:
        s+=i
    return s

def ex(a,b):
    return a if a>b else  b


def main():
    print(sum(1,2,3))
    print(sum(4,1))
    print(sum(1))
    list1=[1]*10
    list2=['h','h,','h','h']
    list2=list2+list1
    list1=list1+list2
    print(list2)
    print(list1)
    array=[1, 2, 5, 3, 6, 8, 4]
    print(array[1::2])
    print(array[2::1])
    print(array[::-1])
    for i in range(0, len(array) - 1, 1):
        print(i)
        for j in range(0,len(array) - 1 - i):
            print(j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print(array)
    print()
    print(ex(b=5,a=3))
    print(ex(a=3,b=5))
    print(ex(5,3))
    print(ex(3,5))
    tuple=("12","l",'plo',894)
    print()
    print(tuple)
    print(tuple)
    set1={"WAV","JPG",'MP3','FLAC','MP3','WORD'}
    set2={"WAV","JPG",'MP4','PPT'}
    print(set1)
    print(set2)
    print(set1&set2)
    print(set1|set2)
    print(set2-set1)
    print(set1-set2)
    print(set1^set2)
    students={"1":"LLK","2":"POL",'9':'OIU','34':'OPI'}
    for i in students:
        print(i,":",students[i])
    if '34' not in students:
        print('true')
    else:
        print('false')
    d={x:x**2 for x in range(1,10,2)}
    print(d)
    for i in d:
        print(i,";",d[i])

    stu1=StudentsInfo()
    print ("ID:%s Name: %s"%(stu1.id,stu1.name))
    stu1.setName("Lzk")
    stu1.setID("10369")
    print("ID:%s NAME:%s"%stu1.getPersonalInfo())


    stu2=StudentsInfo("10965","ploj")
    print("ID:%s NAME:%s"%stu2.getPersonalInfo())

    stu2.selectCourse("高等数学")
    stu2.selectCourse("python程序设计")
    stu2.selectCourse("python程序设计")
    stu2.selectCourse("python程序设计")
    stu2.selectCourse("python程序设计")
    for course in stu2.courseList:
        print(course)
    print(stu2.name)
    print(stu2.id)
    f=open("x.txt",'w')
    f.write("""    for i in p:
        s+=i
    return s

def ex(a,b):
    return a if a>b else  b

def main():
    print(sum(1,2,3))
    print(sum(4,1))
    print(sum(1))
    list1=[1]*10
    list2=['h','h,','h','h']
    list2=list2+list1
    list1=list1+list2
    print(list2)
    print(list1)
    array=[1, 2, 5, 3, 6, 8, 4]
    print(array[1::2])
    print(array[2::1])
    print(array[::-1])
    for i in range(0, len(array) - 1, 1):
        print(i)
        for j in range(0,len(array) - 1 - i):
            print(j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print(array)
    print()
    print(ex(b=5,a=3))
    print(ex(a=3,b=5))
    print(ex(5,3))
    print(ex(3,5))
    tuple=("12","l",'plo',894)
    print()
    print(tuple)
    print(tuple)
    set1={"WAV","JPG",'MP3','FLAC','MP3','WORD'}
    set2={"WAV","JPG",'MP4','PPT'}
    print(set1)
    print(set2)
    print(set1&set2)
    print(set1|set2)
    print(set2-set1)
    print(set1-set2)
    print(set1^set2)
    students={"1":"LLK","2":"POL",'9':'OIU','34':'OPI'}
    for i in students:
        print(i,":",students[i])
    if '34' not in students:
        print('true')
    else:
        print('false')
    d={x:x**2 for x in range(1,10,2)}
    print(d)
    for i in d:
        print(i,";",d[i])

    stu1=StudentsInfo()
    print ("ID:%s Name: %s"%(stu1.id,stu1.name))
    stu1.setName("Lzk")
    stu1.setID("10369")
    print("ID:%s NAME:%s"%stu1.getPersonalInfo())


    stu2=StudentsInfo("10965","ploj")
    print("ID:%s NAME:%s"%stu2.getPersonalInfo())

    stu2.selectCourse("高等数学")
    stu2.selectCourse("python程序设计")
    stu2.selectCourse("python程序设计")
    stu2.selectCourse("python程序设计")
    stu2.selectCourse("python程序设计")
    for course in stu2.courseList:
        print(course)
    print(stu2.name)
    print(stu2.id)
    f=open("x.txt",'w')
    str=""
""")
    f.close()
    f=open("x.txt",'r')
    for str in f:
        print(str,end = '')
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    f.close()
    f=open("x.txt",'r')
    while str:
        str=f.read(15)
        print(str)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    f.seek(100,0)
    str=f.read()
    print(str)
    f.close()
    sumFromScreen()
    str="123456"
    sys.stdout.write(str)
    sys.stdout.write('\n')
    sys.stderr=open("log.txt",'w')
    print(4/0)
    sys.stderr.close()
 
   
    
main()
