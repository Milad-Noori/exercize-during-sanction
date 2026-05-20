from colorlog import exception
from cryptography.hazmat.asn1.asn1 import sequence
from scipy.stats import pearsonr
from setuptools.command.alias import alias

# counter = 0
# mylist= [1,2,3,4,5,6,7,8,9]
#
# for i in mylist:
#     counter+=1
#     if  i % 2 == 0 :
#         print(f" {i} adad zoj ast")
#
#     else:
#         print(f" adad {i} fard ast")


# for m in "milad is the best developer":
#     big =  m.upper()
#     print(big)

#
# mylist = [1,2,3,[1,2.3,4],'milad','alo']
#
# for i in mylist:
# print(mylist[::])

#
# people = (('milad',26),('ali',14),('majid',20))
#
# for name,sen in people:
#     print(name,sen)


# list = {'jadi':[45,140],'milad':[26,178],'ali':[20,180]}
# for i in list:
#     print(i,list[i][0])

# dic = {'hassan': [26,180] , 'jafar' : [50,170] , 'samira': [20,150] , 'mahdi':[10,140]}
# # for body ,data in dic.items():
# #     print(f"{body} ===>{data} ")
# # for data in dic.keys():
# # #     print(f" ===>{data} ")
# for a in dic.values():
#     print(f"{a}")
# for b in dic.keys():
#     print(f"{b}")
# a = 0
# while a <  5:
#     print(f"a is {a}")
#     a = a+1


# b = 0
# while  b<=100 :
#     print(f"a is {b}")
#     b += 1
#
# print("model is finished")
# print(f"the last number was {b}")
# fuel = 0
# check = "check the charge"
# more = "situation is ok"
# tesla = int(input("enter the km of car for charge : " ))
# while tesla > 60:
#     print("our tesla car is has enogh charge")
#     print(f"{more}")
#     break
#
# while tesla < 50:
#     print("No charge")
#     print(f"please {check}")
#     break


# fuel = 4
#
# while fuel <= 100:
#     print(f"your  have {fuel}")
#     fuel+= 1
#
#
# print("your charge is full please put out the charger")


# for c in [1,2,3,4,5,6,7,8,9]:
#     if a == 3:
#         break
#     print(a)

# for i in range(1,9):
#     pass
#
# tip = "in var bazar"
# for k in tip:
#     if i == 6:
#         break
#     print(i)


# list = [3,5,7,9,6,5,8,2,6,9,10]
# list.sort()
# print(list)
#
# for i in list:
#     if i == 9 :
#         continue
#
#     print(i)
#

#
# print("starting")
#
# for a in [1,2,3,4,5,8,[3,5,6],9]:
#     if a == 6 :
#         continue
#     print(a)
# print("ended")


# for i in range (1 ,20):
#     if i % 3 ==0  and  i % 5 == 0 :
#         print("hiphop")
#         continue
#     if i % 3 == 0 :
#         print("HOP")
#         continue
#     if i % 5 == 0 :
#         print("Hip")
#         continue
#     print(f" {i}")


# a = 0
# while a < 20 :
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(f"{a} ")


# for i in range (1 ,50):
#     if i % 5 == 0 :
#         continue
#     if i % 2 == 0 :
#         continue
#
#     if i % 3 == 0:
#         print("that's True")
#
#     print(f"{i}")


# list = [0,1,0.2,4,0.6]
#
# new_list = [x * 2 for x in list ]
#
# print(new_list)

# for i in range (6):
#     for j in range(6):
#         print(i*j , end = '\t')
#     print(i)


# for i in range (1,20,2):
#     print(i)
#
#
# for k in range (10,1,-1):
#     print(k)


# l = "milad is a developer"
# print(len(l))
# for i in range(len(l)):
#     if len(l) == 20:
#         print(i)
#     else:
#         print("namojod")

# for i in range(len(l)):
#     print(i,l[i])


#
# new = [1,5,19,'milad','ali',9,7]
#
# for i in range(len(new)):
#     print(i,new[i])

# name = ['ali','milad','jafar']
# family = ['hosseini','javadi','noori']
# age = [16 , 18 , 20]
#
# # for k in zip(name,family,age):
# #     print(i)
#
#
# for i in zip(name,family,age):
#     print(i)


# new = ['jadi','noori','hosseini']
# char= 'abcdefghijk'
#
# if 'o' in char:
#     print('bood')
# else:
#     print("nist")
# new = ['jadi','sara','mohammad']
# p = {
#     'jadi': {'sen':45,'ghad':180},
#     'sara': {'sen':20,'ghad':140}
#       }
#
# if 'sara' in p:
#     print("I have")


# esm = ['mahdi','mmad','taghi']
# dic = {
#         'mahdi':{'sen':15 , 'color':"white"},
#          'mmad':{'sen' :20, 'color':"black"}
#
#       }
# if 'sen' in dic:
#     print('yes')


# javab = randint(1,5)
# hads = int(input("Enter a number :"))
# if hads == javab :
#     print("hads shoma dorost ast")
# else:
#     print(f"Sorry")
#


# team = {'hasan':1 , 'milad':2 , 'moslem ':3}
# javab = randint(1,3)
# if javab == 1 :
#     print('hassan')
# elif javab == 2 :
#     print('milad')
# elif javab == 3:
#     print('moslem')


# def hello():
#     print("hello world")
#
# hello()

# def hello(name):
#     for a in range(len(name) ):
#         print(f"oh my name is {name}")
# hello("milad")
#
#
#
# def hello(name):
#     '''
#     this item if very famous for our hello system for any
#     option for developers that try to handle some bugs.
#     '''
#     for i in range(len(name)):
#         print(f"my name is {"name"}")
# hello("karim")


# def avg_of_some(num1 , num2 ):
#     for i in range (1,4):
#         print(num1 + num2)
#         print(num1 * num2)
# avg_of_some(avg_of_some(7 ,6))


# def star_logo():
#     for i in range (1,8):
#         print("*")
#         i += 1
#         for j in range(i):
#             print("*")
#             j += 1
#             return i
# star_logo()


# def number_saver (num1 , numb2):
#     '''
#     this is a simple calulator
#     :return:
#     '''
#     jam = num1 + numb2
#     zarb= num1 * numb2
#     taghsim = num1 / numb2
#     tavan  = num1 ** numb2
#     print(jam,'',zarb,'',taghsim,'',tavan)
#     return zarb(5,6)
# # number_saver(5,6)


#
# def calculater (a , b):
#     res = a + b
#     print(res)
#     return res
# calculater(5,6)


# def peida_kon(s,c):
#     counter = 0
#     for kashef in s :
#         if kashef == c :
#             counter +=1
#     return counter
# sentence = "milad is really powerfull ,
# milad is from afghanistan and milad  is a developer "
# print(f"the {sentence}has {peida_kon("milad is really powerfull
# , milad is from afghanistan and milad  is a developer " ,"kashef")}" , "a")


# def calculater():
#     num1 = int(input("enter number :"))
#     num2 = int(input("enter number :"))
#     person = int(input("Type : "))
#
#     jamadad = 1
#     mehaadad = 2
#     zarbadad = 3
#     taghsimadad = 4
#
#     if person == 1 :
#         jam = num1 + num2
#         print(jam)
#     elif person == 2 :
#         menha = num1 - num2
#         print(menha)
#     elif person  == 3 :
#         zarb = num1 * num2
#         print(zarb)
#     elif person == 4:
#         taghsim = num1 / num2
#         print(taghsim)
#
# calculater()


# def say_hello(name , n):
#     for i in range (n):
#         print(f"salam {name} ")
#
# say_hello("milad",3)
# say_hello("reza",1)

# from random import  randint
# fruit = ['mooz','khiar','goje','piaz']
#
# entekhab = int(input("mive morede nazar ra entekhab knid :"))
#
# def kharid_kardan():
#     for i in range(1):
#         if entekhab == 1:
#             print("mooz")
#         elif entekhab == 2 :
#             print("khiar")
#         elif entekhab == 3 :
#             print("goje")
#         elif entekhab == 4 :
#             print("piaz")
#         else:
#             print("mive mojod nis ")
# kharid_kardan()

# jomle = input("jome khod ra vared konid:")
# def upper_case ():
#
#     res = jomle.upper()
#     number = jomle.count("m")
#     return res
# print(upper_case())

# def sum_of_numbers (a, b):
#     res = a + b
#     return res
# n1 = 5
# n2 = 9
# print(sum_of_numbers(n1 , n2))

# def print_time(name , n =3 ):
#     '''
#     this method is suitable for calling  right after  then we can point out
#     how many times we print the name.
#     '''
#     for i in range (n):
#         print(name)
# print_time('milad')


# def is_even (n):
#
#     this function show us is one number even or odd it's very important to handle this problem
#     in order ot discover the mystrys of world.

#
#
#     if n % 2 == 0 :
#         print("is even")
#
#     else:
#         print("is not even")
#
# print(is_even(5))


# def is_even (nums):
#     counter = 0
#     for n in nums:
#         if n %2 == 0 :
#             count = count + 1
#     return counter
# count = is_even([2,4,5,6,7,8])
# print(count)


# def odd_number_finder(mydata):
#     odd = []
#     zoj =[]
#     for n in  mydata:
#         if n %2 ==0 :
#             zoj.append(n)
#         else:
#             odd.append(n)
#     return odd , zoj
#
# mydata = [1,5,6,7,8,9,13,12,20]
# my_list = odd_number_finder(mydata)
# print(my_list)


# def kharid_noon(tedad):
#
#
#     this method is for buying bread from bakery
#     with this moudle you can understand better
#
#     count = 0
#     for i in tedad:
#
#         if i == 1:
#             return  "yek adad non"
#         elif i == 2:
#             return  "two adad non"
#         elif i == 3:
#             return  "se adad non"
#         elif i == 4:
#             return  "chahar adad non"
#         elif i == 5 :
#             return  "are you from afghanistan?"
#
#     return i
#
#
# noon =[1,2,3,4,5]
# tedad_noon = kharid_noon(noon)
# print(tedad_noon)

# from random import randint
#
# def roshan_kardan(hads):
#         res =randint(1,2)
#         if randint == adad:
#             return "system roshan shod"
#         else:
#             return "No one"
#
#         return res
#
# adad = [1,2]
# adad_hadsi = roshan_kardan(adad)
# print(adad_hadsi)


# assume = 0
# number = 0

# def wellcome():
#     '''
#     valuble fuction for introduce the number it is essential for developer to understand betrer.
#
#     '''
#
#     print("wellcome to my game !!!")
#     print("it is not easy for normal people ")
#     return
#
# print(wellcome())
#
#
# def user_input(assume):
#
#     '''
#     this is for guess the number for user with this function user can add a number !!
#
#     '''
#
#     int(input("Entry your number :"))
#     return assume
# print(user_input(assume))
#
# def choose_number():
#     number = random.randint(1,20)
#     return number
# print(user_input(number))
#
#
#
# def answer(assume ,number):
#     if assume > number :
#         return "your assume is to large"
#     elif assume< number :
#         return "the number is smaller than your guess"
#     else:
#         return  "you win bro"
#
# print(answer(assume,number))
#
#
# def win(assume , number):
#     return  assume == number
#
# print(win(assume ,number))
#
#
#
# while  (not win( assume,number )):
#     gess = answer()
#     wellcome()
#     win()
#


#
# def math(*args):
#     res = 1
#     for k in args:
#         res *= k
#     return res
# b = math(5,3,6,7,8)
# print(b)


# def mesal (**kwargs):
#     return kwargs
#
# # b = mesal()


# def calculate_cicle(p , r ):
#     masahat  = p * r * r
#     return masahat
# result = calculate_cicle(3.14 , 7)
# print(result)


#
# def tavan_2 (x):
#     return x ** 2
#
# a = [2,3,4,5]
# tavan_2_a = map(tavan_2, a)
# print(tavan_2_a)

# def tavan_3 (x):
#     return x ** 3
# b = [1,5,6,9]
# tavan_3_a = map(tavan_3,b)
# print(list(tavan_3_a))
# # for i in tavan_3_a:
# #     print(i)


### lambda

#
# a = [5,4,7,9,3]
#
# tavan_2 = map(lambda x: x ** 2, a )
#
# print(list(tavan_2))

# def is_ashari(x):
#     return x  == int(x)
#
# a = [1.3,2,3.3,4,5.8,9.1]
# filter_ashari = filter(is_ashari, a)
#
# print(list(filter_ashari))


# name = ['milad','sina','ali','jalal','farhad','mmd']
#
# short_names = filter(lambda x : len(x) <= 3 , name)
# print(list(short_names))


# class newclass():
#     def __init__(self,param1):
#         self.param1 = param1
#         print('object created')
#     def say_hello(self):
#         print(f"hello")
#
#
#
# milad = newclass(100)
# print(milad.param1)
# print(type(milad))


#
# class book():
#     def __int__(self,page):
#         self.pages = page
#
# mybook = book(180)
# mybook.pages


#
# class maddrese():
#     def __init__(self,danshamoz):
#         self.daneshamoz = danshamoz
#
#
# school = maddrese("44")
# print(school.daneshamoz)
#
#
# class book ():
#     def __init__(self,page):
#         self.pages = page
#
# newbook= book('800')
# print(newbook.pages)
# print(school.daneshamoz)


# class person ():
#     def __init__(self,name , age ,id):
#         self.name = name
#         self.age = age
#         self.id = id
#
# new_person = person("milad",25,"25d2ss")
# print(new_person.name)
# print(new_person.age)


# class car():
#     def __init__(self,model , color , value ):
#         self.moodel = model
#         self.color = color
#         self.value = value
#
#         def arrive(self):
#             print(f"the ({model}) with ({color}) is started")
#
#
# car_model_type = car.model = "bmw"
# car_color_type = car.color = "blue"
# car_value_type = car.value = "300"
# print(car_model_type,car_color_type,car_value_type)
#
# model = car("Benz","gold","400")
# print(model.color)


# class home():
#     def __init__(self,price,meter,room):
#         self.price = price
#         self.meter = meter
#         self.room = room
#
#
# myhome = home.price = 10
# myroom = home.room = 2
# mymeter = home.meter = 100
#
#
# print(myhome,myroom,mymeter)


#
# def football():
#     player_number = input('Entery number:')
#     player_name = input('Entry the name of player')
#     shoot = 0
#
#     if  player_number < 5 :
#         print(" you are defa")
#         shoot += 1
#     elif player_name > 6 :
#         print("you are attaker ")
#     else:
#         print("Nothing")
#
#     return shoot
#
# football()


#########################################################################################
# _________________________________________oop_____________________________________________

# class robotic():
#     def __init__(self,hand,eye,body,prompt):
#         self.hand = hand
#         self.eye = eye
#         self.body = body
#         self.prompt = prompt
#
#     def move(self):
#             print(f"when my {self.eye} is open please give me a {self.prompt}. ")
#
#
#
# b1 = robotic("left","green-eye","move","requist")
# print(b1.move())

################################################################################################
# class book():
#     def __init__(self,name,page):
#         self.name = name
#         self.page = page
#
#     def open(self):
#         print(f"the book name is {self.name} and {self.page}pages")
#
#
# b1 = book("python-30" ,220 )
# print(b1.open())
#
# class darsi(book):
#     def __init__(self, paye , reshte , name, page):
#         book.__init__(self,name, page  )
#         self.paye = paye
#         self.reshte = reshte
#         print("a new darsi book")
#     def open(self):
#         print(f" open {self.name} , and  page {self.page } in major {self.reshte}")
#
# d = darsi("sevom","yajrobi","zist", 120)
# # print(type(d))
# # print(d.page)
# # print(d.name)
# # print(d.paye)
# # print(d.reshte)
#
# print(d.open())

########################################################################
#
# class basketball():
#     def __init__(self, name , height):
#         self.name = name
#         self.height = height
#     def action(self):
#         print(f" the {self.name} has {self.height}")
#
# basketbal_player = basketball("ali",190)
# basketbal_player.action()


# class runner():
#     def __int__(self, name , height):
#         self.name = name
#         self.height = height
#
#     def action(self):
#         print(f" the {self.name } is {self.height}")
#
#
# milad = runner("milad" , 170)
# milad.action()


#
# class runner():
#     def __init__(self, name , height):
#         self.name = name
#         self.height = height
#     def action(self):
#         print(f" the {self.name} has {self.height}")
#
# runner_player = runner("milad",100)
# runner_player.action()
#
#
# for person in [runner_player , basketbal_player]:
#     person.action()
#

###############################################################################

# class file ():
#     def __init__(self, pdf, svg , png ):
#         self.pdf = pdf
#         self.svg = svg
#         self.png = png
#     def data(self):
#         print(f" type of data is {self.png} or {self.pdf}, or {self.svg}")
#
# all_type = file("ketab" , "aks","jozve")
# all_type.data()


# class png( file ):
#     def __init__(self, name ):
#         self.name = name

# _________________________________ import package _________________________________________
# pip install package
# import st from st
import emoji

# print(emoji.emojize("python is : red_heart:",language='alias'))
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# from time import sleep
# from tqdm import tqdm
# for tqdm in range(100):
#     sleep(0.1)
#
# print(tqdm)


# ----------------------------------------module---------------------------------------------

# def play_video_game ():
#     counter = 0
#     while   counter < 5 :
#         print(f" number of  counter is {counter}")
#         counter += 1
#
#
# print(play_video_game())


# from milad import test_module

# _______________________________________________ Error Handle _________________________________

# try:
#     prit("this is a test")
#
# except:
#     print("we have an error.")


# def deveis (a,b):
#
#     try:
#         return a / b
#     except exception as e:
#
#         print(f"we have error , e = {e}")
#         return None
#
#
# print(deveis(2 , 2))
# print(deveis(10,4))


# try:
#     f = open("tmp/myfile")
# except FileNotFoundError:
#     print("finding file breakdown")
# except:
#     print("another error")


#____________________________________________ unit test _____________________________________________________

# def count_m(s , c):
#     counter  = 0
#     for char in s:
#         if char == c :
#             counter += 1
#     return counter

#_______________________________________________________________________________________________________________

# class  metro_station():
#     def __init__(self,people,station,destiny):
#         self.people = people
#         self.station = station
#         self.destiny = destiny
#
#     def dorbin (people):
#         counter = 0
#         woman = []
#         men = []
#         for person in range(1,100):
#             if person % 2 == 0:
#                 woman.append()
#             else:
#                 men.append()
#             counter =+ 1
#         return woman,men,counter
#
# new = metro_station('milad' , 'beheshti' ,'sohrevardi')
# print(new.dorbin())
# print()

import collections
from collections import Counter



mydata = [1,2,3,1,4,5,7,2,3,4,5]
Counter(mydata)
print(Counter)













