# # a='qwert123'
# # s=('q','2','4')
# # d=['w','1','2','5']
# # f={'y','e','q','3'}
# # g={'name':'小柒','are':'女','log':'12'}
# # print('q'in a)
# # print('q'in d)
# # print('log'in g)
# #
# # money=77
# #
# # if(money<=100):
# #     print('找富婆')
# # elif(money<200):
# #     print('何智彬鸭鸭包邮')
# # elif (money<1000):
# #     print('李森林吹牛b')
# # elif(money<10000):
# # #     print('森林当鸭')
# # # else:
# # #     print('让国服瑶妹当鸡')
# # #
# # # for i in range(100):
# # #     print(i)
# # #     print('找富婆')
# # #
# # # print(list(range(1,2)))
#
# # i=2
# # while(i<20):
# #     print(i)
# #     i += 1
#
# # while True:
# # #      print('')
#
# for i in range(1,11):
#     if i in [1,3,6]:
#         continue
#     print(i)
#     print('森林骚')
#
# for i in range(1,11):
#     if i in [1,3,6]:
#         continue
#     print(i)
#     print('找富婆')
# # -*- coding: utf-8 -*-
#
# for m in range(1,10):
#
#     for n in range(1,10):
#
#         print('%s×%s=%s'%(m,n,m*n))
#         for i in range(1, 10):
#             for j in range(1, i + 1):
#                 print('{}x{}={}\t'.format(j, i, i * j), end='')
#             print()
# for i range(1,11)
#
#
# def div(a,b):
#     if (b == 0):
#         print('shao')
#     else:
#         print(a / b)
# div(3,0)
# div(4,9)
#
# def shao(gfhl):
#     res = '7'
#     return  res
# a = shao('')
# print(a)

# def s(a,b):
#     return a+b
# c = s(3,7)
# print(c)

# def a(t=1,o=2):
#     return t/o
# print(a(1,3))

# def s(a,*args,b=10,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# s(1,2,4,5,6,7,name="shao",age=10,b=2)



# i%10 == 5 个位数去5
# i//10%10 == 5 十位数去5
# i//100%10 == 5 百位数去5
# # i //1000 ==5 千位数去5
# for i in range(1,10001):
#     if (i%10 == 5 or i//10%10 == 5 or i//100%10 == 5 or i //1000 ==5):
#         continue
#     print(i)

# q = open('a.txt','w')
# q.write('hdfdfh')
#
# c=10
#
# def a():
#     global c
#     c=20
# a()
# print(c)
#
# a='123,45,678,90，261,91,125'
# a=a.replace('，',',')
# print(a.split(','))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} x {} = {}'.format(j,i,j*i),end='\t')
#     print()
#
# q=[1,23,4,5,6,7,8,9,0]
# q[0]=10
# q.append(1000000)
# q.insert(3,999)
# import random
# #
# l = [10,1,35,61,89,36,55]
# # 依次比较相邻的两个数据，如果前边的数据比后边的大， 则交换两个数据的位置，直到把最大的数据都放到最后第一次排序结束，
# 第二次排序重复第一次排序的动作，把第二大的放到倒数第二的位置，依次类推，直到所有的数据都排好序为止


# for i in range(len(l)-1,0,-1): # i代表最后一个未排好序的数据下标
#     for j in range(0,i): # j 代表每次循环时，当前位置的下标
#         if(l[j] > l[j+1]): # 比较当前位置和下一个位置的数据大小，如果当前位置大于下个位置，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]  # 交换两个数据的位置
#
# print(l)

# i%10 == 5 个位数去5
# i//10%10 == 5 十位数去5
# i//100%10 == 5 百位数去5
# i //1000 ==5 千位数去5
# for i in range(1,10001):
#     if (i%10 == 5 or i//10%10 == 5 or i//100%10 == 5 or i //1000 ==5):
#         continue
#     print(i)
# i = 1
# while(i<10):
#      print(i)
#      i += 1
# #打印出100以内可以被3整除的数
# # for i in range(1,101):# i在1-100这个范围内依次取值
# #     if (i % 3 == 0):# 如果i除以3取余是0,(表示可以除尽)
# #         print(i)#可以得到
#
# #计算1-100的和 即1+2+3....+100
# # a=0#赋值
# # for i in range(1,101):#i在1-100这个范围内依次取值
# #     a+=i   #(等同于a=a+i a+=1等同于a=a+1)
# # print(a)
#
# class s_xin():
#
#     a = 8
#
#     def replace(self):
#         print('1')
#
#     def split(self):
#         print('李森林JJN')
#
# # sx=s_xin()
# # sx.a='dis'
# # sx.replace()
# # sx.split()
# import  requests
# # '''
# 1、编写一个返回随机手机号的方法
# def phoe():
#     import random
#
#     q = random.choices("0123456789", k=8)
#     print(('135')+(''.join(q)))
# phoe()
#
# import random
# a=('134','187','199','178')
# d=random.choice(a)
# #print(d)
# f=random.choices('1234567890',k=8)
# g=''.join(f)
# #print(g)
# print(d+g)

# def phoe():
#     s=("135","189","178","199","134")
#     a=print(random.choice(s))
#     #print(a)
#     q = random.choices("0123456789", k=8)
#     f=''.join(q)

#
# # 2、编写一个返回指定长度和内容的随机字符串方法
# # def s6():
# #     import random
# #     q = random.choices("0123456789ggfdgfrh", k=6)
# #     print(''.join(q))
# # s6()
#
# def s6(s,d):
#     import random
#     q = random.choices(s,k=d)
#     print(''.join(q))
# s6("jfdfdjf34325",5)

# 3、
# 编写一个返回随机姓名的方法
# '''
# 100逢七过 7的倍数或者以7结尾就说过
# for i in range(1,101):
# import random
#
#
# def random_name():
#     xing_list = ["赵","钱","孙","李","周","武","郑","王","欧阳","诸葛","轩辕","上官","司徒"]
#     zi_list = "花赤橙黄绿青蓝紫冬梅建国华世凯"
#     xing = random.choice(xing_list)
#     zi_length = random.randint(1,2)
#     res = random.choices(zi_list, k=zi_length)
#     zi=''.join(res)
#     return xing + zi#return此将数据返回random_name
#
# print(random_name())
# print('我正测登陆')
# try:
#     r = open('t.txt','r')
# except (Exception) as 错误详情1:
#     print(错误详情1)
#     print('报错1')
# try:
#     print(1 / 0)
# except (Exception) as 错误详情2:
#     print(错误详情2)
#     print('报错2')
# else:
#     print("整个程序没错")
# finally:
#     print('不管有没错误都运行')
# print('测试结束')


s='123678356598'
l='687987'
print(s)
