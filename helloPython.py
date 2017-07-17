
import random
import sys
import os
import types

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
# list类型的数据可以方便的增查删改，正因为方便操作，所以更占内存

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
# 这里是对文件的操作
# write_file = open('test.txt', 'wb')
# write_file.write(bytes('Write me to the file', 'UTF-8'))
# print(write_file.mode)
# print(write_file.name)
# write_file.close()

#
# read_file = open('test.txt', 'a+')
# # print(text_in_file)
# read_file.writelines('Hello')
# text_in_file = read_file.read()
# print(text_in_file)
# read_file.close()


# f = open('test.txt', 'w+')
# # f.write(bytes('apple', 'UTF-8'))
# all_the_Text = f.read()
# print(all_the_Text)
# f.close()

# start:stop:step   这个是list的切片操作

# aList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(aList[1:])
# print(aList[:-1])
# print(aList[3:8])
# print(aList[0:aList.__len__():2])    # a：b：c  表示从a下标到b下标，每隔c遍历一次
# print(aList[::5])


class Animal:
    _name = ''
    _height = 0
    _weight = 0
    _sound = 0

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def set_sound(self, sound):
        self._sound = sound

    def get_sound(self):
        return self._sound

    def __init__(self, name, height, weight, sound):
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self._name,
                                                                      self._height,
                                                                      self._weight,
                                                                      self._sound)


cat = Animal('Tomato', 30, 7.5, 'Meow')
print(cat.toString())


class Dog(Animal):  # Dog继承于Animal
    _owner = ''

    def __init__(self, name, height, weight, sound, owner):
        self._owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self._owner = owner

    def get_owner(self):
        return self._owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} The owner is {}".format(self._name,
                                                                                      self._height,
                                                                                      self._weight,
                                                                                      self._sound,
                                                                                      self._owner)

    def multi_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog('Spotdog', 50, 16, 'bark', 'Seino')
spot.toString()


#
# class Bare(Animal):
#


class Animal_Testing:
    def get_type(self, animal):
        animal.get_type()


test_Animal = Animal_Testing()
test_Animal.get_type(cat)
test_Animal.get_type(spot)


class Haski(Dog):
    _attack = 0

    def __init__(self, name, height, weight, sound, owner, attack):
        self._attack = attack
        super(Haski, self).__init__(name, height, weight, sound, owner)

    def set_attact(self, attack):
        self._attack = attack

    def get_attack(self):
        return self._attack

    def get_type(self):
        print('Haski, a kind of dog')

    def toString(self):
        print("{} is {} cm tall and {} kilograms and says {}, owner is {}, attack is {}".format(self._name,
                                                                                                self._height,
                                                                                                self._weight,
                                                                                                self._sound,
                                                                                                self._owner,
                                                                                                self._attack))

    def isInt(self, num):
        return [True, False][type(num) == type(1)]

    def check(self, num):
        tag = True
        if type(num) != type(1):
            tag = False
        return tag

    def cast_damage(self, atk_times):
        damage_health = atk_times * self._attack
        if atk_times is None:
            print('You still safe')
        else:
            if damage_health < 100:
                print("You just been attacted by {} times still got {} health".format(atk_times, 100 - damage_health))
            elif damage_health >= 100:
                print("You totally got killed")


kk = Haski('KK', 50, 15, 'Haha', 'Seino', 25)
kk.toString()
print(kk.cast_damage(3))
# print(kk.check(20))
