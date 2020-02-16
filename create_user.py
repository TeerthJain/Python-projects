
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:25:58 2020

@author: Teerth Jain
"""
import sys
print("Wwelcome to Rock Paper Scissors, made by Teerth\n")
yes_or_no = input("Do you want to create a user ((y)es or (n)o: ")
if yes_or_no == 'n':
    sys.exit()
while True:

    username = input("Please pick a username: ")
    password = input("Please pick a password: ")
    pass_confirm = input("Please confirm the password: ")
    
    if password != pass_confirm:
        print("Please try again")  
    elif password == pass_confirm:
        text_file = open('people.txt', 'a')
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        print("User account has been successfully created")
        break
        
            
    
    


