#coding:utf-8
###引用
##内建函数id可以查看变量的地址
##a,b都是100这个对象的引用
#a = 100
#b = a
#print id(a)
#print id(b)
##a的地址改变，而不是a里面的内容改变
#a = 200
#print id(a)

##while循环
#count = 0
#while count < 5:
#    print count
#    count += 1
    
###for循环
##打印字符串
#a = "1234"
#for c in a:
#    print c
##打印列表
#b = [1, 2, 3, 4]
#for value in b:
#    print value
##打印字典
#c = {'a':1, 'b':2}
#for key in c:
##print可以不止打印一个元素，只要加逗号即可，默认输出以空格分隔
#    print key,c[key]

##内建函数range可以生成一个数字组成的列表
#for i in range(0, 10):
#    print i
##第三个参数是步长
#for i in range(0, 10, 2):
#    print i
##步长可以为负数
#for i in range(10, 0, -2):
#    print i

###break和continue
##找出[0,99]中的第一个3的倍数
#for i in range(0, 100):
#    if i % 3 == 0:
#        break
#print i
##找出[0,99]中的所有3的倍数
#for i in range(0, 100):
#    if i % 3 != 0:
#        continue
#    print i

##空语句-》pass
#for i in range(0, 10):
#    if i % 2 == 0:
#        pass
#    else:
#        print i

##生成[0,4]每个元素的平方，放到列表中
#a = [i * i for i in range(0, 5)]
#print a
#b = [i ** 2 for i in range(0, 5)]
#print b
##获取[0,4]中奇数的平方
#c = [i * i for i in range(0, 5) if i % 2 == 1]
#print c

###函数
##def定义，return返回结果
#def add(x, y):
#    return x + y
#
#print add(10, 30)
#print add("hello", "may")
##python中函数没有"重载"的说法
#def Func():
#    print "aaa"
#def Func():
#    print "bbb"
#Func();

##python支持默认参数
#def Func(debug = True):
#    if debug:
#        print "in debug mode"
#    else:
#        print 'done'
#Func()
#Func(False)

##解包语法-》函数返回多个值
#def GetPoint():
#    return 10, 20
#x, y = GetPoint()
#print x,y
##_可以做占位符
#_, z = GetPoint()
#print z

##函数也是对象，也可定义别名来引用它
#def Func():
#    print 'hello'
#func = Func
#func()
#Func()
#print type(func)

###文件操作
##内建函数open-》打开一个文件
##以只读方式打开文件file.txt
#f = open("file.txt", mode = 'r')
#print type(f)
#for line in f:
##不加","，会多出空行,因为每行的字符串有个'\n'
#    print line,
##不关闭会文件描述符泄露
#f.close()
#
#f = open("file.txt", mode = 'r')
#words = {}
#for word in f:
#    word = word[:-1]#去掉末尾的'\n'
#    if word not in words:
#        words[word] = -1
#    else:
#        words[word] += 1
#f.close()
#print words

##import关键字-》引用其他.py文件中的代码
#import add
#print add.Add(1, 2)
#a = add
#print a.Add(1, 2)
#
#from add import Add
#print Add(2, 3)
#
##打印模块查看的路径
#import sys
#print sys.path
