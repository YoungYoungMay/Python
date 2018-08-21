#!/usr/bin/python
#coding:utf-8

####文件操作

###文件的基础操作
#
##内建函数open->打开文件
#f = open('./file', 'r')
#f.close()
#
##读文件
#f = open('./file', 'r')#以读方式打开
##for line in f:
##    print line,#默认打印一行会加一个空行，所以加,避免空行出现
##print f.readlines() #读整个文件返回一个列表,每个元素为字符串是一行数据->换行符会保留
#for line in f.readlines():
#    pint line.strip() #去掉读取到的换行符
#f.close()
#
##写文件
#f = open('./file1', 'a')#以追加写方式打开
#f.write('this is YoungMay\n')
#f.close()


###操作文件指针
#
##文件具有随机访问的能力->通过文件指针完成
#seek/text

##with语句 && 上下文管理器
#    #-》语句块结束，可以自动释放文件描述符
#with open('./file', 'r') as f:
#    for line in f:
#        print line,
#print 'read done'


##基于一个简单文本，构造一个大文本(构造测试数据)????
#import sys
#imput_file_path = sys.argv[1]
#output_file_path = sys.argv[2]
#output_size = int(sys.argv[3])*1024*1024
#input_file = open(input_file_path)
#input_data = input_file_readlines()
#output_file = open(output_file_path, 'w')
#index = 0
#total_size = 0
#while True:
#    if total_size > output_size:
#        break
#    output_file.write(input_data[index % len(input_data)])
#    total_size += len(input_data[index % len(input_data)])
#    index += 1

###文件系统的基础操作

##文件路径操作
#import os.path
#path = '/home/may/Code/Python/class4/file'
#print os.path.basename(path)   #打印文件名(去掉路径)
#print os.path.dirname(path)    #打印路径(去掉文件名)
#print os.path.split(path)      #返回(dirname(), basename())元组
#print os.path.splitext(path)   #返回(filename(), extension())元组

#import os
#path = '/home/may/Code/Python/class4'
#for basedir, dirname, filenames in os.walk(path):
#    print basedir
#    print filenames
#    print dirname
#    print '---------'

##常用文件系统操作
#
##生成一个“hello world”文件，并执行
#import os,stat
#if os.path.exists('hello.py'):
#    os.remove('hello.py')
#os.mknod('hello.py')
#f = os.open('hello.py', os.O_RDWR)
#os.write(f, '#!/usr/bin/python\nprint "hello world"')
#os.close(f)
#os.chmod('hello.py', stat.S_IRUSR|stat.S_IXUSR)
#os.system('./hello.py')
#
##实现ls命令
##!/usr/bin/python
#import os,sys
#path = sys.argv[1]
#for f in os.listdir(path):
#    print f,
#
##遍历目录下所有目录和文件
#import os,sys
#path = sys.argv[1]
#for root, dirnames, filenames in os.walk(path):
#    for filename in filenames:
#        print os.path.join(root, filename)
