#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#learn judement sentence
# True and False

#if ture:                #lowercase ?  no no
#    print('true')
if True:
    print('True')

#if elif else sentence
print('----------------------------------')
age = 15
if age >= 15:
    print('teenage')
else:
    print('child')

print('----------------------------------')

age2 = 133

if  age2 >= 0 and age2 <= 16:
    print('child')
elif  age2 > 16 and age2 <= 45:
    print('adult')
else:
    print('old guy')

string_null = ''
list_null = []

if not 0:
    print('not 0 True')

if not string_null:
    print('not string null true')
    print('string null ', string_null)
if not list_null:
    print('not list null true')
    print('list_null ', list_null)
print('----------------------------------')

#input block function
age3 = input("please input a num:")      #input get a string
age_int = int(age3)
if  age_int <= 0 or age_int >= 160:
    print('NOT HUMAN!!!')
elif  age_int > 0 and age_int <= 16:
    print('child')
elif  age_int > 16 and age_int <= 45:
    print('adult')
else:
    print('old guy')






