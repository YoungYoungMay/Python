#coding:utf-8
#python练习题

##使用while循环输出0-10
#count = 0
#while count <= 10:
#    print count
#    count += 1


##使用for循环输出0-10
#for i in range(0, 11):
#    print i


###用户输入一个字符串，举个字符显示出来
#
##while实现
#str = raw_input("Enter str:")
#size = len(str)
#i = 0
#while i < size:
#    print str[i]
#    i += 1
#
##for实现
#str = raw_input("Enter str:")
#for j in str:
#    print j


##用户输入一个数字，判断这个数字是正数/负数/0
#num_str = raw_input("Enter num:")
#num = int(num_str)
#if num == 0:
#    print "是0"
#elif num < 0:
#    print "是负数"
#else:
#    print "是正数"


##创建一个包含5个数值的列表，通过用户输入确定每一个值，并计算五个数的平均值???
#aList = list()
#for i in range(5):
#    num = raw_input("Enter num:")
#    aList.append(int(num))
#i = 0
#sum = 0
#size = len(aList)
#while i < size:
#    sum += aList[i]
#    i += 1
#print sum / size 


##猜数字游戏???
#import random
#key = random.randint(1, 100)
#i = 0
#while i < 100:
#    x = int(raw_input("guess number:"))
#    if key == x:
#        print "bingo"
#        break
#    elif x < key:
#        print "too small"
#    else:
#        print "too big"


##带文本菜单的程序-》由用户选择执行相应的功能
##菜单选项如下：1.求5个数的和 2.求5个数的平均值....(X).退出
#arr = list()
#for i in range(5):
#    num = raw_input("Enter num:")
#    arr.append(int(num))
#i = 0
#sum = 0
#size = len(arr)
#while i < size:
#    sum += arr[i]
#    i += 1
#
#while True:
#    input = raw_input("choose:")
#    if input == "1":
#        print sum
#        break
#    elif input == "2":
#        print sum / size
#        break
#    elif input == 'X':
#        print "退出菜单"
#        break
#    else:
#        print "选择错误，请重新选择"
