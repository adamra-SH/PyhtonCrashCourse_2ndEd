# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:17:01 2019

@author: adamra
"""
###############################################################################
#   Part 1 - The Basics                                                       #
###############################################################################

                                                                    # Chapter 1
"""Setting up Programming Environment

Open the anaconda terminal and type [python] to get to the interpreter >>>
We have python 3.6.4"""

#T_ermin_al commands:
    python = enter the interpreter
    ctrl z = exit # go back to command prompt
    exit() = exit

print("Hello Python world!")

                                                                    # Chapter 2
""" Variables and simple data types"""

# creating variable 'message'
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print (message)

""" Rules and guidelines when usin variables to keep code easy to read
- variable names CAN contain only letters, numbers and underscores
    -CANNOT start with a number
-spaces are not allowed in variable names so use underscores(_)
-avoid using Python keywords and function names"""
    KEYWORDS
    -False  await  else     import    pass    None    break     except  in      raise
    -True   class  finally  is        return  and     continue  for     lambda  try
    -as     def    from     nonlocal  while   assert  del       global  not     with
    -async  elif   if       or        yeild
    FUNCTIONS
    -abs()    all()    any()    ascii()    bin()    bool()    breakpoint()
    -bytearray()    bytes()    callable()    chr()    classmethod()    compile()
    -complex()    delattr()    dict()    dir()    divmod()    enumerate()  
    -eval()    exec()    filter()    float()    format()    frozenset()    
    -getattr()    globals()    hasattr()    hash()    help()    hex()    id() 
    -input()    int()    isinstance()    issubclass()    iter()    len()    list()
    -locals()    map()    max()    memoryview()    min()    next()    object()
    -oct()    open()    ord()    pow()    print()    property()    range()    
    -repr()    reversed()    round()    set()    setattr()    slice()    sorted()
    -staticmethod()    str()    sum()    super()    tuple()    type()    vars()
    -zip()    __import__()

# Upper case variables have specific meanings (so be carful)

# Strings
name = 'ada lovelace'
print(name.title())

--title is a method
print [value] (which is the name variable) .title (act on the [value] with title method)

print(name.upper())
print(name.lower())
# if storing strings from users, you will want to use lower because you cannot
# trust what your users have sent you. Then adjust your case when needed.

#Using variables in strings using f{}... these are called f strings (format strings)
    #if using earlier versions of Python (prior to 3.6), then use format()
    # syntax example full_name = "{} {}".format(first_name, last_name)
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

message = f'Hello, {full_name.title()}!'
print(message)
# THese types of layers allow your code to look much cleaner AND allow for reusability

White space:
    spaces   = ' '
    tabs     = '\t'
    new line = '\n'
    
print('Python')
print('\tPython')
print('Languages:\nPython\nC\nJavascript')

print('Languages:\n\tPython\n\tC\n\tJavascript')

# removing extra white space can be very helpful as well when you're comparing 
# data, so using a strip command is helpful

favorite_languange = 'python '
favorite_languange
favorite_languange.rstrip()
favorite_languange # key note that the variable has NOT been reassigned with 
                    # the stripped string
favorite_languange = favorite_languange.rstrip()
# This above will reassign the variable favorite_language

favorite_languange = ' python '
favorite_languange.lstrip()
favorite_languange.rstrip()
favorite_languange.strip()

# apostrophe errors
# double quotes will allow you to put apostrophe's within the string
message = "One of Python's strengths is its diverse community."
print(message)

message_error = 'One of Python's strengths is its diverse community.'
print(message_error)

# integers

2+3
3-2
2*3
3/2

# ** is exponent
3**2
3**3
10**6
 
# you can use order of operations
2+3*4
(2+3) *4
8/2(2+2) # why doesnt this work?

# you can mix ints and floats

1 + 3.0

# Under scores to group your numbers without affecting them py3.6 or later
universe_age = 14_000_000_000
print(universe_age)

# you can quickly assign multiple variables at once
x, y, z = 0, 0, 0 # separate with commas

# Python doesnt have 'constants', but you will use all caps to indicate this

MAX_CONNECTIONS = 5000 # THIS INDICATES that the variable should not be changed

""" Main reason to write comments is to explain what your code is supposed to be
doing and how you're making it work. Write how you came up with the solution"""

import this #Zen of Python, by Tim Peters
                                                                    # Chapter 3
# you should name lists plurally, meaning use letter(s), digit(s), or name(s)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#lists are indicated with brackets []
print(bicycles) #prints your list exactly as you entered it

#picking out individual 'elements' in a list
print(bicycles[0]) #removes all and only selects the element in index 0
print(bicycles[0].title()) # capitalize the first of every word

#combine f-string with the list and making a string
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# test
names = ['Preston', 'Ryan', 'Rochelle', 'Benson']
for l in names:
    print(f"{l}'s first bike was a {bicycles[0].title()}.")
# Above was a quick test of fstring and a for loop with a single bike

#Adding, changing, or removing elements
    #Changing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

    #Adding
motorcycles.append('ducati')
print(motorcycles)

#   append() allows you to create lists dynamically
motorcycles = [] #create an empty list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

    #Removing
        #Using del
            #Used when you know the specific index of the element
del motorcycles[0]
print(motorcycles)
del motorcycles[0]
del motorcycles[-1]
print(motorcycles)

    #Removing
        #Using pop() method
            #Pop removes the last item in a list, but lets you work with it after
            # removing it - term pop comes from thinking of a list as a stack
            # of items and popping one item off the top of the stack     -pg.39
motorcycles = [] #create an empty list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#The last motorcycle I bought was? (not a huge fan of this)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

        #popping a position
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# Important to know whether to use the del or pop, ask yourself if you want to
    # use that element again or not

    #Removing
        #Using remove() method
            #Removing item by its value
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)#this does not loop through all instances, just hte first one
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

                        ##### Try it Yourself #####

#Creating a guest list for at least three people
guests = ['Preston', 'Benson', 'Rochelle']

# Send out invitation to each individual
print(f"{guests[0]}, would you be able to make it for dinner?")
print(f"{guests[1]}, would you be able to make it for dinner?")
print(f"{guests[2]}, would you be able to make it for dinner?")

print(f"{guests[2]} won't be able to make it!")

# replace rochelle with leonardo (rochelle couldnt make it)
guests[2] = 'Leonardo'
#reprint guest list
print(f"{guests[0]}, would you be able to make it for dinner?")
print(f"{guests[1]}, would you be able to make it for dinner?")
print(f"{guests[2]}, would you be able to make it for dinner?")
#let the current guests know you're inviting more
print(f"{guests[0]}, I found a bigger dinner table so I will invite a few more, ok?")
print(f"{guests[1]}, I found a bigger dinner table so I will invite a few more, ok?")
print(f"{guests[2]}, I found a bigger dinner table so I will invite a few more, ok?")

# insert new guests
guests.insert(0, 'Raphael') # insert, inserts before the index specified
guests.insert(1, 'Donnatello')
guests.append('Mikey') # append adds to the end of the list

print(f"{guests[0]}, would you be able to make it for dinner?")
print(f"{guests[1]}, would you be able to make it for dinner?")
print(f"{guests[2]}, would you be able to make it for dinner?")
print(f"{guests[3]}, would you be able to make it for dinner?")
print(f"{guests[4]}, would you be able to make it for dinner?")
print(f"{guests[5]}, would you be able to make it for dinner?")

# remove 4 guests because your table will not arrive until after the dinner
# print a sorry that you will not be able to invite them
mikey = guests.pop()
print(f"{mikey}, I am sorry I cannot invite you this time.")
leo = guests.pop()
print(f"{leo}, I am sorry I cannot invite you this time.")
ben = guests.pop()
print(f"{ben}, I am sorry I cannot invite you this time.")
pres = guests.pop()
print(f"{pres}, I am sorry I cannot invite you this time.")

print(f"{guests[0]}, you're still invited!")
print(f"{guests[1]}, you're still invited!")

                        ##### End #####

# Organizing a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # default is aalphabetical          PERMANENTLY
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # this is sorted BUT NOT PERMANENT

print("\nHere is the original list again:")
print(cars)

# Sorting a list alphabetically is complicated when all the values are not in
    # lowercase 
    
# reversing the list order (not sorted)     PERMANENT
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding Length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

                                                                    # Chapter 4
# Working with lists
    # FOR LOOPS
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# examples of how to write the temp variable (make it meaningful)
    
for cat in cats:
for dog in dogs:
for item in list_of_items:

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')    
    print(f'I can"t wait for the next trick, {magician.title()}.\n')
    
print(f'Thank you, everyone. That was a great show!')
    
# indent error without error
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')    
print(f'I can"t wait for the next trick, {magician.title()}.\n')
    
# Numerical Lists
for value in range(1,5): # Starts at 1 and ends BEFORE 5, so 1-4
    print(value)

numbers = list(range(1,5))
print(numbers)

                        # start, stop, multiple (by 2's)
even_numbers = list(range(2,11,2))
print(even_numbers)

# Create the square of a list of numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# More concisely written
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Simple statistics
min(squares)
max(squares)
sum(squares)

# List comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

# Slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # player 0, 1, 2
print(players[:4]) # the first 4, so 0, 1, 2, 3
print(players[-3:]) # starts at the 3rd from last and on

# looping through players slice

print("Here are my first three players:")
for player in players[:3]:
    print(player.title())

# copying a list
my_foods = ['pizza', 'spaghetti', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_foods)

#This ^ above is different than doing my_foods = friends_foods because this 
    # cannot be appended separately!!
    
# Creating and working with Tuples
    #Tuples are immutable, they cannot be changed so lets say you had a rectangle
    #you didnt want changed
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# looping tuple is same as list:
for dimension in dimensions:
    print(dimension)

# writing over a tuple, modifying it by reassigning it
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

                        #####Try it yourself#####
foods = ('chicken salad', 'new york strip', 'chicken tenders', 'shrimp', 'a taco')
for food in foods:
    print(f"{food.title()} is one of our top 5 items on the menu!")
#should not work**
foods[1] = 'salad'

#New Menu
foods = ('shrimp salad', 'porter house', 'chicken tenders', 'shrimp', 'a taco')
for food in foods:
    print(f"{food.title()} is one of our top 5 items on the menu!")
                        #####      END      #####

Styling your CODE:
    Indentation - make sure that your tabs are 4 spaces
    Line length - 80 characters or less --> the line is 80!
    Blank Lines - are used to group parts of your code together
                                                                    # Chapter 5
# If statements, deciding to do one thing or another
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# a single = sign is a statement, like setting the cars to something
# double = signs is comparing

#Checking for inequalities
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Testing numbers
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21
age <= 21
age > 21
age >= 21

#checking multiple conditions

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_1 = 22
age_0 >= 21 and age_1 >= 21
 # can be replace with -or- as well
 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings # results true
'pepperoni' in requested_toppings # results false

#Lets ban some users from something

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# boolean

game_active = True
can_edit = False

#simple if statements

age = 19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if else statements
age = 17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, but you're not old enought vote yet.")
    print("Come back when you're 18 and register!")

# admission to an amusement park
age = 12

if age < 4:
    print("Your admission fee is $0.")
elif age <18:
    print("Your admission fee is $25.")
else:
    print("Your admission fee is $40.")

#more concise method
age = 12

if age < 4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40
print(f"Your admission fee is ${price}.")

# multiple elif's (as many as you want!)
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission fee is ${price}.")

#testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

                    #####     Try it youself     #####
# alien shot down in game
alien_color_1 = 'green'

if alien_color_1 == 'green':
    print('5 POINTS!')
elif alien_color_1 == 'yellow':
    print("10 POINTS!")
elif alien_color_1 == 'red':
    print("15 POINTS!")

# stages of life
preston = 14

if preston < 2:
    print("You're a baby!")
if preston < 4:
    print("You're a todler!")
if preston < 13:
    print("You're a kid!")
if preston < 20:
    print("You're a teenager!")
if preston < 65:
    print("You're an adult!")
if preston >= 65:
    print("You're an elder!")

                    #####     END                #####

#checking for special conditions

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# else if
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we're out of {requested_topping}")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# dealing with an empty list

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# comparing a list of available toppings to the requested list
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']
        #This could have been a tuple ^^
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we do not have {requested_topping}")
print("\nFinished making your pizza!")

                    ##### Try it yourself #####
users = ['Ryan', 'Benson', 'Preston', 'Admin', 'Rochelle']

for user in users:
    if user == 'Admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again!")
        
# Empty user list, doing if users is the check for empty list. Then create loop
        # for normal usage afterwards

users = []

if users:
    for user in users:
        if user == 'Admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again!")
else:
    print("We need some users!")
    
# creating list and ensuring they are unique user names

current_users = ['ryan', 'rochelle', 'benson', 'preston', 'travis']
new_users = ['sally', 'nolan', 'Benson', 'lilly', 'preston']

for new_user in new_users:
    if new_user.lower() in current_users: #use lower to make sure case is not a problem
        print("User name is already in use, please try again.")
    else:
        print(f"{new_user.title()} is perfect for you!")

# ordinal numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")
                    
                    ##### End             #####
                    
                                                                    # Chapter 6
# Dictionaries
# Simple dictionaries
                                                                    
# you can have unlimited number of keys ex- color, points...
alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

# accessing dictionary values

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key value pairs
    # This can be done at any time!

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# an empty dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# modifying values in dictionary

alien_0 = {'color':'green'}
print(f'The alien is {alien_0["color"]}.')

alien_0 = {'color':'yellow'}
print(f'The alien is now {alien_0["color"]}.')

# lets modify the dictionary and move the alien around based on its speed

alien_0 = {'x_position':0, 'y_position': 25, 'speed':'medium'}
print(f'Original position: {alien_0["x_position"]}')

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New position: {alien_0["x_position"]}')

# change the speed to fast
alien_0['speed'] = 'fast'

# you can store about a single object (the alien) or results like a poll

# similar objects
favorite_languanges = {
        'jen': 'python', 
        'sarah':'c', 
        'edward':'ruby', 
        'phil':'python'
        }
language = favorite_languanges['sarah'].title()
print(f'Sarah"s favorite language is {language}.')

# looping through all key value pairs (looping a dictionary)
user_0 = {
    'username': 'efermi', 
    'first': 'enrico',
    'last': 'fermi'
    }

print(user_0['username']) # single piece of information

# list comprehension
for key, value in user_0.items(): # all info about user
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# list comprehension for looping
favorite_languanges = {
        'jen': 'python', 
        'sarah':'c', 
        'edward':'ruby', 
        'phil':'python'
        }
#    key, value        dictionary         method
for name, language in favorite_languanges.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through just the keys
for name in favorite_languanges.keys():
    print(name.title())

# lets pick out certain friends and give them a different message

friends = ['phil', 'sarah']
for name in favorite_languanges.keys():
    print(f" Hi {name.title()}")
    
    if name in friends:
        language = favorite_languanges[name].title() # creates list of languages for friends
        print(f"\t{name.title()}, I see you love {language}!")

# lets see if a certain person took the poll
        
if 'ryan' not in favorite_languanges.keys():
    print("Ryan, please take our poll!")

# sorting the keys in the dictionary

for name in sorted(favorite_languanges.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# what about just the values of the dictionary
    # this can be repetitive and clutters the list
print("The following languages have been mentioned:")
for language in favorite_languanges.values():
    print(language.title())

# just values without the repetition of a dictionary
print("The following languages have been mentioned:")

#               set doesnt allow for repetition
for language in set( favorite_languanges.values()):
    print(language.title())

# nesting
    # an alien_0 dictionary contains only info about that alien, not many
    
# how to do this
# first create dicts for each alien
    
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color':'yellow', 'points': 10}
alien_2 = {'color':'red', 'points': 15}

# now store them in a list 

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# more realistic example would have more than 3 aliens with code that AUTOMATICALLY
    # creates these aliens. We will use range() to create 30 aliens
    
# make an empty list to store aliens.
aliens = []

# make 30 green aliens
for alien_number in range(30): # how many aliens we want
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# show the length of aliens created
print(f"There are {len(aliens)} in this list")

# now that we have 30 different objects in this list, even though they are the same
    # lets change the first 3 aliens to faster ones

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# show first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# lets include turning the yellow into red faster ones

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# show first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# storing a list inside a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
    }

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
        "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# you can nest a list inside a dictionary any time you want more than one value
    
favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'], 
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }

for name, languages in favorite_languages.items():
    # each name has potentially multiple languanges, so you have to loop through
    # those as well using another loop inside a loop!
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# lets change it to say language if they only have one, like Sarah!
for name, languages in favorite_languages.items():
    if len(languages) >1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")

# dictionary within a dictionary
    # unique users for a website

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
    
for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    
                                                                    # Chapter 7
# using the input() function
# while loops to keep programs running as long as certain conditions remain true

message = input("Tell me what you want me to repeat back to you? ")
print(message)

# be very clear about what you want from a prompt
    # users will need to know exactly what to input

name = input("Please enter your name: ")# the space after the colon makes it clear
print(f"\nHello, {name}!")

# writing a prompt thats longer than one line
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# what about integers? well lets use int()

age = input("How old are you? ") # input automatically creates a string
age # string

age >=18 # error because its a string comparing to an int

# turn their input into an int

age = int(age)
age >= 18 # returns True because it is!

# lets ride a roller coaster!

height = input("How tall are you? ")
height = int(height)

if height >=48:
    print("\nYou're tall enough to ride this ride.")
else:
    no_message = "\nI am sorry, but you're not tall enough to ride this ride,"
    no_message += " come back when you're older!"
    print(no_message)

# using the modulo operator (%)
    # doesnt tell you how many times it was divided by, but tells you the remainder
    # determine if a number is odd or even
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

                        ##### Try it Yourself #####
# rental car company

car_requested = input("What kind of car would you like?")
car_requested = car_requested.lower()
cars_available = ['subaru', 'toyota', 'gmc', 'chevy']
upper_list = ['bmw', 'gmc']

if car_requested in cars_available:
    if car_requested in upper_list:
        car_requested = car_requested.upper()
    print(f"You have great taste and we can get the {car_requested.title()} ready!")
else:
    if car_requested in upper_list:
        car_requested = car_requested.upper()
    print(f"Really unfortunate, but we do not have the {car_requested.title()} available right now.")

# multiple of ten test

number = input("Tell me a number, and I'll tell you if its a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a muliple of 10, boo!")

# is a number able to be multiplied by a certain number
number = input("Tell me a number to divide: ")
number = int(number)
m_number = input("Tell me the number to divide it by: ")
m_number = int(m_number)

if number % m_number == 0:
    print(f"The number {number} is a multiple of {m_number}.")
else:
    print(f"The number {number} is not a muliple of {m_number}, boo!")

                        ##### End #####



















