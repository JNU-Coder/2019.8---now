#1.给set集合增加数据
person ={"student","teacher","babe",123,321,123}
person.add("student") #如果元素已经存在，则不报错，也不会添加,不会将字符串拆分成多个元素，区别update
print(person)
person.add((1,23,"hello")) #可以添加元组，但不能是list
print(person)
'''
{321, 'babe', 'teacher', 'student', 123}
{(1, 23, 'hello'), 321, 'babe', 'teacher', 'student', 123}
'''
 
person.update((1,3)) #可以使用update添加一些元组列表，字典等。但不能是字符串，否则会拆分
print(person)
person.update("abc")
print(person)  #会将字符串拆分成a,b，c三个元素
'''
{321, 1, 3, 'teacher', (1, 23, 'hello'), 'babe', 'student', 123}
{321, 1, 3, 'b', 'c', 'teacher', (1, 23, 'hello'), 'a', 'babe', 'student', 123}
'''
 
#2.从set里删除数据
person.remove("student")#按元素去删除
print(person)
#print("student")如果不存在 ，会报错。
'''
{321, 1, 3, 'c', 'b', (1, 23, 'hello'), 'teacher', 'babe', 'a', 123}
'''
person.discard("student")#功能和remove一样，好处是没有的话，不会报错
person.pop() #在list里默认删除最后一个，在set里随机删除一个。
print(person)
'''
{1, 3, (1, 23, 'hello'), 'teacher', 'b', 'a', 'babe', 123, 'c'}
'''
#3.更新set中某个元素,因为是无序的，所以不能用角标
#所以一般更新都是使用remove,然后在add
 
#4.查询是否存在，无法返回索引，使用in判断
if "teacher" in person:
    print("true")
else:
    print("不存在")
'''
true
'''
#5.终极大招：直接清空set
print(person)
person.clear()
print(person)
'''
set()
'''
