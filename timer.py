# -*- coding: utf-8 -*-
"""
Created on Tuesday Feb 18 18:11:40 2020

@author: Teerth Jain
"""
import tkinter
import time
password_list = []
from user_check import user_check
from user_check import user_check
print("Welcome to Teerth's Timer...")
sleep1 = time.sleep(1)
print("Loading file...")
sleep1
print("...")
sleep1
a = tkinter.Tk().bell()
user = input("Please enter your username: ")
password = input("Please enter your password: ")
time.sleep(2)
file = open('people.txt', 'r')
for line in file:
    password_list.append(line.strip())
    if user and password in password_list:
        print("Access Granted")
        sleep1
        times = int(input("What is the duration of your timer(Secs)... "))
        print(f"We are setting up a timer of {times} seconds...")
        start = input("Press (s) to start...")
        if start == 's':
            while times > 0:
                print(f'{times} seconds left...')
                time.sleep(1)
                times -= 1
                if times <= 0:
                    x = 0
                    while x < 25:
                        tkinter.Tk().bell()
                        time.sleep(0.3)
                        x += 1

    if password and user not in password_list:
        print("Sorry we could'nt find and user of your name, please create a user")
