#!/usr/bin/python

#This program says hello and assk for my name

print('Hello World')
print('What is you name?') #ask for the user name
myName = input()
print('It is good to meet you, ' + myName + '.')
print('How do you pronounce ' + myName + ' in your native language.')
print('The length of your name is: ' + str(len(myName)) + '.')
print('What is your age? ' + myName + '.')
myAge = input() #ask for the users age
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
