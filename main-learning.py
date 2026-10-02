## OOP - Object-Oriented Programming
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle") #Changes shape to a turtle
# timmy.color("DarkOrchid") #Changes color
# timmy.forward(100) #Moves forward
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick() #Makes the Screen close upon detecting a click

## Pypi
# https://pypi.org/
# File > Settings > Python > Interpreter

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
# table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
# table.align = "c"
# print(table)

## Creating a Class
# class User: #PascalCase
#     def __init__(self, user_id, username): #Initialize attributes. New objects must pass the parameters
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001", "robert")
# # user_2 = User()
# # user_2.id = "002"
# # user_2.username = "anna"
# user_2 = User("002", "anna")
#
# user_1.follow(user_2)
#
# print(user_1.following)
# print(user_1.followers)
# print(user_2.following)
# print(user_2.followers)

## Class Inheritance
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale. Exhale.")
#
# class Fish(Animal): # Inheriting from class "Animal"
#     def __init__(self):
#         super().__init__() #super accesses the Class we're inheriting from
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#
#     def swim(self):
#         print("moving in water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

## Slicing
piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#            |    |    |    |    |    |    |    |
#            0    1    2    3    4    5    6    7
print(piano_keys[2:5])
print(piano_keys[:5])
print(piano_keys[2:5:2]) #The third number specifies the increment.
print(piano_keys[::2]) #This will cut off every second item
print(piano_keys[::-1]) #This will print all items, but in reversed order
# Slicing also works on Tuples