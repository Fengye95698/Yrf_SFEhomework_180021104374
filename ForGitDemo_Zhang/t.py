list1 = []
list2 = []
list3 = []
list_all = []


def mode(n):
    if n < 10:
        for m in range(n):
            list_all.append(m + 1)
        print(list_all)
    elif n % 10 == 0:
        count = int(n / 10)
        for i in range(count):
            for j in range(10):
                list1.append((j + 1))
            list_all.append(list1[:10])
        print(list_all)
        # list3.append(list_all)
    else:
        count = int(n / 10)
        if count <= 10:
            for i in range(count):
                for j in range(10):
                    list1.append((j + 1))
                list_all.append(list1[:10])
            # list3.append(list_all)
            for k in range(n % 10):
                list2.append(k + 1)
            list_all.append(list2)
            # list3.append(list2)
            print(list_all)
        else:
            for i in range(count):
                for j in range(10):
                    list1.append((j + 1))
                list_all.append(list1[:10])
                if len(list_all) > 10:
                    list3.append(list_all)
            # list3.append(list_all)
            for k in range(n % 10):
                list2.append(k + 1)
            list3.append(list2)
            print(list3)
    # print(len(list_all))


def main():
    # enter = input("请按任意键开始，N/n结束")
    # while enter not in ['n', 'N']:
    num = eval(input("请输入元素总和："))
    mode(num)
    # enter = input("请按任意键开始，N/n结束")


# 1 0-4
# 2 4-8
# 3 8-12
# 4
# p = input()
# for i in p:
#     if ord('a') <= ord(i) <= ord('z'):
#         print(chr(ord('a') + (ord(i) - ord('a') + 3) % 26),end='')
#     elif ord('A') <= ord(i) <= ord('Z'):
#         print(chr(ord('A') + (ord(i) - ord('A') + 3) % 26),end='')
#     else:
# x = ''
# string = input()
# for i in string:
#     if 'a' <= i <= 'z':
#         x = (ord('z')+ord('a')-ord(i))
#         print(chr(x),end='')
#     elif 'A' <= i <= 'Z':
#         x = (ord('Z')+ord('A')-ord(i))
#         print(chr(x),end='')
#     else:
#         print(i,end='')
# 1 1 1
# 2 3 3
# 3 5 5
# 4 7 7
# 3 2
# 1 1
# 2 0
#
# 5 3
# 1 2
# 2 1
# 3 0
string = 'Hello'
num = 123456
# print("你好对应的英文是：{:20}".format(string))
# print("你好对应的英文是：{:>20}".format(string))
# print("你好对应的英文是：{:^20}".format(string))
# print("你好对应的英文是：{:*^20}".format(string))
# print("你好对应的英文是：{:2}".format(string))
# print("你好对应的英文是：{:.2}".format(string))
# print("数字的对应显示是：{:.2f}".format(num))
# print("数字的对应显示是：{:,}".format(num))
# print("数字的对应显示是：{:@^20,.1f}".format(num))
# print("数字的对应显示是：{:,.2f}".format(num))
# print("数字的二进制显示是：{:b}".format(num))
# print("数字的十进制显示是：{:d}".format(num))
# print("数字的八进制显示是：{:o}".format(num))
# print("数字的十六进制大写显示是：{:X}".format(num))
# print("数字的十六进制小写显示是：{:x}".format(num))
# print("数字的百分制显示是：{:%}".format(num))
# print("数字的百分制显示是：{:%}".format(num))
# print("数字的百分制显示是：{:e}".format(num))
# t = input()
# # a = eval(t[1:])
# if t.isalpha():
#     print("请输入正确的温度值。")
# elif 0<eval(t[1:])<=10:
#     print("冷")
# elif 10<eval(t[1:])<=20:
#     print("凉爽")
# elif 20<eval(t[1:])<=28:
#     print("舒适")
# elif 28<eval(t[1:])<=38:
#     print("热")
# elif eval(t[1:])>28:
#     print("热死狗啦~~~")
# else:
#     print('寒冷')

# import math
# num = input()
# if num.isalpha():
#     print("请输入正确的参数。")
# else:
#     print("{}的平方根为{}".format(eval(num),math.sqrt(eval(num))))

# i = input()
# # # if i.isalpha():
# # #     print("输入有误！")
# # # elif i[0]=='-':
# # #     print('-{}'.format(i[:0:-1]))
# # # else:
# # #     print(i[::-1])
# a,b = eval(input().split(';'))
# if b==0:
#     print("除零错误")
# else:
#     print("{:.2f}".format(a/b))