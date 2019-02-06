#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
print('hello python3')
#comment

#string code
#ascii 编码是utf8编码的一部分 unicode 编码的效率不是很好

#打印中文字符
print("你好 python")

#字符长度
len1 = len('ab')
print('ab','len is ',len1)

len2 = len('中文')
print('中文','len is ',len2)#default encoding is the unicode

len3 = len('中文'.encode('utf-8'))
print('中文','utf8 code len is ',len3)


#格式化输出
str1 = '张三'
age = 22
print('your name is %s and age is %d' % (str1, age))     #多参数% 后面跟元组没有逗号隔离

