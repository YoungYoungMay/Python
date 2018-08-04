#! usr/bin/env python
#coding:utf-8
##上句使得该文件可写中文注释
###python的简单入门


#print 'hehe'

##定义变量，不建议在表达式后加分号
#count = 0
#pi = 3.14
#name = 'may'
##打印
#print count
#print pi
#print name

##python不支持++/--操作
#count = 0
#count += 1
##这里的++会被当作两个正号
#++count
#count++
#print count

##变量可在运行时改变类型-》即动态类型
#a = 10
#a = 'str'
#print a

##内建函数type可以查看数据的类型
#a = 10
#b = 3.14
#print type(a)
#print type(b)
#a = 1000000000
###b等于a的100次方
#b = a ** 100
#print b

##有一种复数形式
#a = 10 + 5j
#print a
#print a+1

###字符串-》可用单引号、双引号、三引号表示
##打印一句话：My name is 'YoungMay'
#a = "My name is ‘YoungMay'"
#b = 'My name is "YoungMay"'
#print a
#print b
##也可用三引号表示字符串-》两种三引号
##单引号不能与单引号构成的三引号挨在一起了
#c = '''My "name" is 'YoungMay' '''
#print c
##双引号不能与双引号构成的三引号挨在一起了
#d = """My "name" is 'YoungMay'"""
#print d
##双引号会对其中内容转义等，但是单引号不会

###索引操作符[]和切片操作符[:]可获取子字符串
#a = 'abcd'

##字符串的第一个索引值为0，最后一个为-1
##python无字符类型，这里打印的a,b,c,d均是字符串类型
#print a[0],a[1],a[2],a[3]
#print type(a)
#print type(a[0])
##访问下标越界
##print a[100]
##允许下标为负，负数即从后向前数
#print a[-1],a[-2],a[-3],a[-4]
#
##切片操作-》访问前闭后开区间，取字串操作
#print a[1:3]
##区间的前面省略，默认从0下标开始
#print a[:3]
##区间的后面省略，默认取到结尾
#print a[1:]
##区间两个都省略，默认全取
#print a[:]
#print a[:-1]
#
#下句打印不出来
#print a[-1:-3]
#print a[-3:-1]
##区间出现下标越界问题，不会出错，只会取到能取到的元素
#print a[:100]

##字符串拼接-》用+号，不用考虑空间问题
#a = 'hehe'
#b = 'haha'
#print a + b

##重复字符串-》'*'
#mystr = '-'
#print mystr * 20

#无字符类型，单个字符也是字符串类型

##内建函数len-》求字符串长度
#a = 'hehe'
#print len(a)

#格式化字符串-》"%d"
#a = 100
#b = "a = %d" % a
#print b

##python有布尔类型-》True/False
#a = True
#print a
#print type(a)
#
##bool类型的变量，是一种特殊的整型变量
##与整数类型进行运算时，True当作1，False当作0
#a = True
#b = False
#print a + 1
#print b + 1

#对于python2来讲，print可以用语句形式打印，也可用函数形式(带括号)
#但对于python3，print只支持函数形式,所以推荐使用函数形式

###输入与输出
##raw_input函数-》从标准输入获取用户输入
##print函数-》将结果输出到标准输出

##raw_input返回的结果是一个字符串
#num1 = raw_input('num1:')
#num2 = raw_input('num2:')
##返回了字符串，进行的是字符串拼接
#print num1 + num2
##不能将整数与字符串显式相加，除非进行类型转换
##print num1+100
##要想输出结果是int型，可用int函数转换
#print int(num1) + int(num2)

####除法
###传统除法-》结果类型与操作数类型有关
##a = 1
##b = 2
##print a / b
##a = 1.0
##b = 2
##print a / b
##
###地板除-》向下取整
##a = 1 
##b = 2
##print a // b
##a = 1.0
##b = 2
##print a // b
##
##精确除法-》python3中默认除法
#from __future__ import division 
#a = 1
#b = 2
#print a / b

#**表示乘方，python中数据大小无上限，取决于机器内存大小

##比较运算符-》返回结果为布尔值
#print 2 < 4
#print 2 == 4
#print 2 > 4
#print 2 != 4
##可以用连续比较符
#print 3 < 4 < 5
##字符串之间也可以判断字符串内容是否相同
#print 'haha' == "hehe"
#print 'haha' != "hehe"
##字符串也可以比较大小，结果取决于字符串的"字典序"
#print 'haha' < "hehe"

##逻辑运算符-》and/or/not
#print 2 < 4 and 2 ==4
#print 2 > 4 or 2 < 4
#print not 6.2 <= 6


###list列表-》"[]"
#a = [1, 2, 3, 4]
#print a
##列表可以存储任意类型、任意数量的python对象
#b = [1, 'hehe']
#print b
##列表也支持取下标操作
#print a[2], b[1]
##列表也可通过切片操作取子串,方法与上面的切片操作一致
##也可通过下标修改元素
#a[0] = 100
#print a

###tuple元组-》"()"
#a = (1, 2, 3, 4)
#print a
##也可保存不同类型元素
#b = (1, 'may')
#print b
##也可通过下标访问
#print a[3],b[1]
###不可以通过下标改变元组元素
##a[0] = 100
##print a

##字典dict-》"{}",存放键值对，python中的映射数据类型
##pyhton中的键值对是基于哈希表实现的
##键值对间用逗号分隔，键值间用冒号，最后一个键值对后面可加可不加分号
#a = {'ip':'127.0.0.1', 'port':80}
#print a['ip']
