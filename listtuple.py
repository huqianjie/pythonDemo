#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

friends = ['ming', 'zhang', 'wang', 'li']
#len of list
len_friends = len(friends)
print('number of friends is : %d' %len_friends)

#list append insert  and pop

friends.append('huhu')
print("friends :", friends)

#show insert of list
print("###### insert fun of list")
friends.insert(1,'THISINSERT')
print('friends :', friends)

#show pop of list
print('###### pop of list')
friends.pop()           #pop() or pop(INDEX)
print('after pop() friends : ', friends)
friends.pop(1)          #1 is the index of insert content
print('pop insert of friends : ', friends)

#list 可以嵌套的使用。list 中的元素也可以是list

#tuple 元组的使用
print('\n---------------------------tuple-----------------------------')
new_friends = ('aaaa','bbb','cc')            #元组的定义是用 小括号，尝试给元组添加元素看是否会报错
print('new_friends : ', new_friends)
#new_friends.pop()                               #AttributeError: 'tuple' object has no attribute 'pop'

#定义只有一个元素的元组
t = (1,)        #t = (1) //this is int type
print('one ele tuple is : ',type(t) )
print('one ele tuple is : ', t)


#尝试改变tuple中的元素来理解tuple 中的变与不变
t2 = ('a', 'b', ['a','b'])
print('t2 ',t2)
print('------change tuple t2-----')
t2[2][0] = 'c'
t2[2][1] = 'd'
print('t2 ',t2)         #here list is alterable

print('------change tuple t2 again-----')
####t2[0] = 'x'
####print('t2 ',t2)      #TypeError: 'tuple' object does not support item assignment
#tuple 中的元素本省不可变但，list 元素本身的指针是可以换指向的














