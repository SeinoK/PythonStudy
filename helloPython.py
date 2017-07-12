import random
import sys
import os

# print(5 % 2)
# print(5 / 2)
# print(5 // 2)
# print(5 * 2)
# print(5 ** 2)
#
# a = "I'm %s. I'm %d year old, and I have %f $" % ('Vamei', 99, 120)
# print(a)
# print("%.*f" % (4, 1.2), '\n')

# **********************************

# This is usage of list, list is a kind of data structure in python, that you can insert and append new item to a list
# very easily and even something else, so it will occupy more memory

# **********************************
# grocery_list = ['apple', 'pear', 'milk', 'banana', 'table', 'juice']
# print('First Item:', grocery_list[0])
# grocery_list[0] = 'Green apple'
# print('The new first item is', grocery_list[0])
# print('Now is the all item here', grocery_list[0:len(grocery_list)], '\n')
#
# other_event = ['wash car', 'pick up kids', 'cash check']
# to_do_list = [other_event, grocery_list]
# print(to_do_list, '\n')
# print(to_do_list[1][4], '\n')    # this a saw array
#
# grocery_list.append('onion')
# print(to_do_list, '\n')
#
# grocery_list.insert(3, 'seino')
# print(grocery_list, '\n')
#
# grocery_list.remove('seino')
# print(grocery_list, '\n')
#
# grocery_list.sort()
# grocery_list.reverse()
# print(grocery_list, '\n')
#
# to_do_list2 = grocery_list + other_event
# print(to_do_list2, '\n')
# print(len(to_do_list2), '\n')
# print(max(to_do_list2), '\n')
# print(min(to_do_list2), '\n')

# This is the usage of tuple，when you create a tuple that you can change it when it still a tuple, so you can convert it
# to a list and modify it

# my_tuple = (2, 4, 5, 3, 6, 8)
# print(my_tuple, '\n')
# my_list = list(my_tuple)
# my_list.remove(2)
# my_tuple_2 = tuple(my_list)
# print(my_tuple_2, '\n')

# This is the usage of set, a set can not contain two same items, and you can do something like union intersection

# my_tuple = {1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3}
# my_set = set(my_tuple)
# print(my_set)

# for i in range(0, 10):
#     print(i, ' ', end='')
# print('\n')
#
# grocery_list = ['apple', 'pear', 'banana', 'tomato']
# for y in grocery_list:
#     print(y)
#
# num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
# for i in num_list:
#     for j in i:
#         print(j, end=' ')

# i = 0
# while (i <= 30):
#     if (i % 2 == 0):
#         print(i)
#     elif (i == 12):
#         break
#     else:
#         i += 1
#         continue
#     i += 1

#
# print("What's your name")
# name = sys.stdin.readline()
# print('hello', name)

# long_string = "I'll catch you if you fall - The Floor"
# print(long_string[0:4])
# print(long_string[-5:])
# print(long_string[:-5])
# print(long_string[:4] + ' be there')
# # 使用%可以进行格式化的输出，%c指代字符，%s指代字符串，%d指代整数，%f指代浮点数，%.xf其中x表示小数点后面多少位
# print("%c is my %s letter and my number %d number is %.2f" %('X', 'favourite', 12, .35))
#
# print(long_string.capitalize())  # 首字母大写，之后字母小写
# print(long_string.find("floor"))  # 返回所需要找寻的字符串位置，如果没有匹配，返回-1
# print(long_string.isalpha())
# print(len(long_string))
# # long_string = long_string.replace(' ', '*')
# print(long_string.replace('o', '**'))  # 用来替换特定字符串，如果没有，则无法替换
# print(long_string.strip(), '\n')
# quote_list = long_string.split(' ')
# quote_list.remove('-')
# for i in quote_list:
#     print(i)
#
test_file = open('test.txt', 'wb')
print(test_file.mode)
print(test_file.name)
test_file.write(bytes('Write me to the file\n', 'UTF-8'))
test_file.close()