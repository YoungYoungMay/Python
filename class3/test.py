#!/usr/bin/python
#coding:utf-8
#序列与字典之序列

###序列类型操作符
#
##in/not in-》判断一个元素是否在序列中,返回布尔值
#a = [1, 2, 3, 4]
#print 1 in a
#a = 'hehe'
#print 'h' in a
#
##连接操作符“+”-》生成新的序列，不修改原有的
#a = [1, 2]
#b = [3, 4]
#print a + b
#print a
#print b
#
##列表推荐使用extend-》类似“+”，但是修改原有的
#a =[1, 2]
#b =[3, 4]
#a.extend(b)
#print a
#print b
#
##字符串推荐使用join-》类似“+”
#
##重复操作符-》让一个序列符重复N次
#a = [1, 2, 3, 4]
#print a * 2
#print 2 * a

##序列的切片操作
#a = [1, 2, 3, 4, 5]
#print a[::2]
#print a[2]
#print a[1:3]

##字符串翻转->常见面试题
#a = "abcdefg"
#b = a[::-1]
#print b
#print a

###序列内建函数
#
##len：返回序列长度
#a = [1, 2, 3, ]
#print len(a)
#a = [1, 2, 3, 4]
#print len(a)
#
##max：返回序列中最大值
#a = [0, 3, -1, 3]
#print max(a)
#
##min：返回序列中最小值
#a = [1, 2, 3, 4]
#print min(a)
#
##sorted：排序，返回一个有序的序列(输入参数的副本,不修改原有序列)
#a = [1, -3, 4, 0]
#print sorted(a)
#print a
#
##sum：序列元素求和
#a = [-1, 3, 2, 0]
#print sum(a)
#
##enumerate-》同时枚举出下标和值,找到指定元素在列表中的下标
#def Find(arr, x):
#    for i, item in enumerate(arr):#i为下标，item即为对应值
#        if item == x:
#            return i
#    else:
#        return None
#a = [1, 3, 2, 4, 5 ]
#print Find(a, 7)
#print Find(a, 3)
#
##zip函数-》矩阵的行列互换，但是只针对行列相等的矩阵
#x = [1, 2, 3]
#y = [4, 5, 6]
#z = [7, 8, 9, 10]
#print zip(x, y, z)
##常见用法-》构造字典
#key = ('name', 'id', 'score')
#value = ('may', 110, 99)
#d = dict(zip(key, value))
#print d



###sorted可支持自定制排序规则
#
##逆序排序->降序
#a = [1, -3, 4, 0]
#print sorted(a, reverse=True)
#
##按元素的绝对值排序->先返回绝对值，再用sorted排序
#def Cmp(x, y):
#    if abs(x) < abs(y):
#        return -1
#    elif abs(x) > abs(y):
#        return 1
#    else:
#        return 0
#a = [1, -3, 4, 0]
#print sorted(a, cmp=Cmp)
#
##按字符串长度排序
#a = ['aaa', 'bbbb', 'cc', 'd', 'eee']
#print sorted(a, key=len)


###字符串->单双引号都一样,都支持转义,三引号可跨行
#
##字符串实际不可变，只能创建一个新的
#a = 'abcd'
##字符串不可修改
##a[0] = 'f'
#print 'f' + a[1:]
#print a
#
##格式化替换%-》只适用于字符串
#a = 100
#print 'a = %d' % a
#
##原始字符串raw strings-》转义字符不生效的字符串
##在字符串前加上r/R前缀即可表示原始字符串
#print r'hello\nworld'
#print 'hello\nworld'
#
##repr函数-》类似str函数
#    #repr输出的字符串是给解释器看的
#    #str输出的字符串是给用户看的
#a = 1
#print repr(a)
#print type(repr(a))
#
#print str(1.0/7.0)
#print repr(1.0/7.0)
#
#print str('may')
#print repr('may')
#
##反引号与repr函数等价


###string模块的常用函数
#
##字符串合并->join
#a = ['aa', 'bb']
#print ','.join(a)
#print ''.join(a)
#
##字符串分割成列表
#a = 'aa bb cc dd'
#print a.split(' ')
#
##判定字符串的开头结尾
#a = 'this is YoungMay'
#print a.startswith('this')
#print a.endswith('May')
#
##去除字符串开头结尾的空白-》换行/空格/制表符/回车
#a = '   hrllo may   \n     '
#print '[%s]' % a
#print '[%s]' % a.strip()
#
##左对齐/右对齐/中间对齐
#a = 'hello world'
#print '[%s]' % a.ljust(50)
#print '[%s]' % a.rjust(50)
#print '[%s]' % a.center(50)
#
##查找子串-》返回下标
#a = 'hello young may'
#print a.find('may')
#
##替换子串->只能生成新对象，字符串不可变
#a = 'hello world'
#print a
#print a.replace('world', 'python')
#
##判断字符串是纯字母/数字
#a = 'helloworld'
#print a.isalpha()
#
#a = 'hello world'
#print a.isalpha()
#
#a = '1244'
#print a.isdigit()
#
##转换大小写
#a = 'hello may'
#print a.lower()
#print a.upper()

###列表->可变
#
##可用切片操作,访问与修改列表元素
#
##追加元素
#a = [1, 3]
#print a
##append追加一个元素
#a.append([4, 5])
##extend连接->追加多个元素
#a.extend([4, 5])
#print a
#
##删除指定下标元素->del/pop
#a = [1, 2, 3]
#print a
#del a[0]
#print a
#a = [1, 2, 3]
#print a
#a.pop(0)
#print a
#
##按值删除元素->remove
#a = [1, 2, 3]
#print a
#a.remove(3)
#print a
#
##列表比较操作
##要列表元素顺序相等，才相等
#a = [1, 2, 3]
#b = [2, 1, 3]
#print a == b
#
##sort->列表本身改变
#a = [1, 2, -3, 0]
#a.sort()
#print a
#
##列表模拟栈
#a = []
#a.append(1) #入栈操作
#print a[-1] #取栈顶元素
#a.pop()     #出栈操作
#
##列表模拟实现队列
#a = []
#a.append(1) #入队
#print a[0]  #取队首元素
#a.pop(0)    #出队

###列表的深浅拷贝->默认浅拷贝
#
##赋值、切片、list工厂函数都是浅拷贝
#a = [100, [1, 2]]
#b = a
#c = list(a)
#d = a[:]
#print a, b, c, d
#print id(a), id(b), id(c), id(d)
#a[0] = 1
#print a, b, c, d
#a[1][0] = 1000
#print a, b, c, d
#print id(a[1]), id(b[1]), id(c[1]), id(d[1]) #a,b,c,d中的a[1]都是同一对象
#
##深拷贝利用copy.deepcopy实现
#import copy
#a = [100, [1, 2]]
#b = copy.deepcopy(a)
#print id(a[1]), id(b[1])
##不一定调用了copy.deepcopy就会深拷贝，最后还是由Python解释器决定的
#import copy
#a = (100, 'aaa')
#b = copy.deepcopy(a)
#print id(a[0]),id(a[1]),id(b[0]),id(b[1])


##元组->不可变,只读
#
##其实所有的多个对象，按逗号分隔的，其实都是元组
#
##元组不可变指的是元组元素id不可变;但元组元素若是可变对象,则可以修改
#a = ([1, 2, 3], [4, 5, 6])
#a[0][0] = 100
#print a


###字典
#
##键:唯一性;可hash(不可变);
##值:没什么限制
#
##创建字典
#a = dict([('x',1), ('y',2)])
#print a
#c = dict({'x':0, 'z':1})
#print c
#d = dict(zip(['x','y','z'], [1, 2, 3]))
#print d
#b = {}.fromkeys(('x', 'y'), 0)
#print b
#
##访问字典元素
#a = {'x':0, 'y':1}
#for i in a:
#    print i, a[i]
#
##修改字典元素
#a = {}
#a[1] = 100
#print a
#a[1] = 200
#print a
#
##del->删除键值对
#a = {1:100}
#print a
#del a[1]
#print a
#
##clear->清空字典中键值对
#a = {1:100, 2:200}
#print a
#a.clear()
#print a
#
##pop->删除键值对，同时获取到值
#a = {1:100, 2:200}
#print a
#a.pop(1)
#print a
#
##内置函数len->键值对个数
#
##内置对象hash->判断对象是否可hash
#print hash(())
#print hash([])
#
##内置函数items->返回列表，每个元素为一个键值对
#a = {'x':1, 'y':2}
#print a.items()


###集合set->基于字典实现
#
##基本操作
#a = set([1, 2, 3])
#b = set([1, 2, 3, 4])
#print a & b
#print a | b
#print a ^ b  #对称差集
#print b - a  #差集
#
##数据去重
#a = [1, 1, 2, 3, 2]
#print a
#b = set(a)
#print b
