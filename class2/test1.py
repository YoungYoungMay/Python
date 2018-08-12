#!/usr/bin/python
#coding:utf-8

##类型的类型
#print type(type(100))
#print id(type(100))

##None-》特殊类型NoneType的唯一对象
##-》类似于C语言中的NULL
#print type(type)

##下列对象的布尔值是False
    ##None,False,值为0的数,""(空字符串),[](空列表),()(空元组),{}(空字典)
#a = []
#if a:
#    print 'hehe'
#else:
#    print 'haha'

##对象值的比较
##所有内建类型对象都可以用比较操作进行值比较,但比较的双方类型需相同
#a = 'hehe'
#b = 'hehe'
#print a == b

##对象身份的比较
#a = 10
#b = 20
#
##"=="比较操作符
#print id(a) == id(b)
#
##关键字“is”
#print a is b
#
## “is not"
#print a is not b

##对象类型的比较-》type函数
#a = 100
#b = 3.2
#print type(a) == type(b)
#
##type函数的优化
#import types
#a = 100
#print type(a) == types.IntType
#
##内建函数isinstance
#a = []
#print isinstance(a, list)
#a = 100
#print isinstance(a, type(100))

##工厂函数

##python不支持的函数
#char/byte
#指针-》不允许修改地址
#short/long-》于int合在一起了
#double-》用float可表示

#字符串分割：split
#字符串合并：join

###常用内置函数/模块
#
##divmod：返回一个元组，同时计算商和余数
#a, b = divmod(10, 3)
#print a, b
##round：对浮点数进行四舍五入
#import math
#for i in range(0, 10):
#    print round(math.pi, i)
#
##oct()-》将整数转化为八进制字符串
##hex()-》将整数转化为十六进制字符串
#print oct(10)
#print hex(10)

##缩进和悬挂else
#x = -1
#y = 2
#if x > 0:
#    if y > 0:
#        print 'x and y > 0'
##与"x>0"对应
#else:
#    print 'x < 0'

##条件表达式-》替代C中的三目运算符
x, y, smaller = 3, 4, 0
#if x < y:
#    smaller = x
#else:
#    smaller = y
#print smaller
#
##上述用条件表达式写作
#smaller = x if x < y else y
#print smaller

###和循环搭配的else
#和循环搭配的else,在不满足循环条件时才会执行
#
##实现一个函数，从列表中查找指定元素，返回下标
#def Find(arr, x):
#    for i in range(0, len(arr)):
#        if(arr[i] == x):
#            return i
#    else:
#        return None
#a = [1, 3, 5, 4, 6, 7, 2]
#ret = Find(a, 4)
#print ret
#
##实现一个函数，打印出一个数的最大公约数
#def ShowMaxFactor(x):
#    count = x / 2
#    while count > 1:
#        if x % count == 0:
#            print 'largest factor of %d is %d' % (x, count)
#            break
#        count -= 1
#    #if count == 1:
#    else:
#        print x, "is prime"
#
#for i in range(10, 20):
#    ShowMaxFactor(i)

##函数的定义也可以放在其他函数内部
    #但是此时函数的作用域仅在函数内部有效
#def Func1():
#    def Func2():
#        print 'hello'
#Func2()


##函数的参数
#def Hello(x):
#    print x
#Hello(100)
#Hello('hello')
#Hello([1, 2, 3])
#
##传入的参数要能够支持函数内部的各种操作
#def Add(x, y):
#    print x + y
#Add(1, 2)
#Add('hello ', "world")
#Add([1, 2], [3, 4])
##下句不支持
##Add(1, 'hello')
#
##支持给函数参数指定默认参数
#def func(x = 100):
#    print x
#func(1)
#func()
#
##对于有多个默认参数的函数，可以按顺序给某几个参数传参
#def func(x = 0, y = 0, z = 0):
#    print x, y, z
#func()
#func(100)
#func(100, 200)
#func(10, 20, 30)

###关键字参数
    #当函数有多个默认参数，但是想不按顺序的传参时
#
##sorted函数-》排序，默认升序
#a = [1, 3, 4, 2]
#print sorted(a)
##sorted支持自定义排序规则
#
##降序排序
#a = [1, 3, 4, 2]
#print sorted(a, reverse = True)
#
##按元素的绝对值排序
#def Cmp(x, y):
#    if abs(x) < abs(y):
#        return -1
#    elif abs(x) > abs(y):
#        return 1
#    else:
#        return 0
#a = [1, -3, 4, 2]
#print sorted(a, cmp = Cmp)
#
##按字符串的长度排序
#a = ['aaaa', 'bbb', 'cc', 'd']
#print sorted(a, key = len)

##将一个元组或字典，作为参数组，传给函数，实现可变长参数
#
##实现一个打印日志的函数
#
##在参数名前加"*"，*后的内容表示是一个元组
#def Log(prefix, *data):
##使用'\t'分隔的行文本，可以很方便的和Linux上的一些文本处理工具搭配使用
#    print prefix + '\t'.join(data)
#Log('[WARINANG]\t', 'hello', 'YoungMay', 'world')
#
##在参数名前加两个"*"，*后的内容表示是一个字典-》可以使用关键字传参了
#def Log(prefix, **data):
#    print prefix + '\t'.join(data.values())
#Log('[Notice]', ip = '127.0.0.1', port = '80', userid = '1234')


##函数重载
    #-》不存在，后面的会覆盖前面的
#日志/错误级别

