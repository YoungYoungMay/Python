#!/usr/bin/python
#coding:utf-8
#python语法

##True与False是变量，而非关键字，也可以交换
#True, False = False, True
#if True:
#    print "hehe"
#if False
#    print "haha"

##内建函数globals()-》全局作用域下有哪些变量
##内建函数locals()-》局部作用域下有哪些变量
#a = 100
#def Func():
#    x = 0
#    print globals()
#    print locals()
#print 'In Global'
#print globals()
#print locals()
#print 'In Func'
#Func()

##特殊标识符
##下划线作为变量的前缀/后缀，表示特殊的标识符
#from add import *
##"_xxx"表示私有变量，使用上句无法导入
#_Add(1, 2)

##文档字符串-》在函数/类的起始位置用三引号表示的多行注释
##文档字符串一定要放在函数/类的开始位置
#def Func():
#    '''这是一个测试函数'''
#    print 'hehe'
#
###查看帮助文档
##print Func.__doc__
##内建函数help也可以做到
#help(Func)

#unix起始行-》指定程序的执行方式

##模块文档-》一个模块也可以有文档字符串
#import add1
#print add1.__doc__

