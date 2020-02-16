
import sys, time, random
print("Created by Teerth Jain")
print("Welcome to the Rock Paper Scissor game")
print("\n\n")
password_list = []
drew = 'You Drew'
lose = 'The computer wins'
win = 'You win'
comp_lives = 5
lives = 5
draws = 0
score = 0
words = ['rock', 'paper', 'scissors']
while True:
    user = input("Please enter your username: ")
    password = input("Please enter your password: ")
    time.sleep(1)
    file = open('people.txt', 'r')
    for line in file:
        password_list.append(line.strip())
        if user and password in password_list:
            print("Access Granted")
            time.sleep(0.5)
            print("...")
            print("Loading...")
            time.sleep(0.5)
            print("Loaded...\n")
            print("""You start with 5 lives.
                  If you loose you loose a live.
                  If you draw the lives stay the same.
                  The first one to get to 0 lives looses.
                  -------------------------------------------
                  Type rules to see rules of the game.
                  -------------------------------------------
                  You can know the live score, draws, lives
                  or the comp_lives by typing show score, etc.
                  -------------------------------------------
                  Type exit to exit the game at any point of time.
                  -------------------------------------------
                  The computer has lives as well
                  Let's see who wins...
                  Good Luck.""")
            while True:                
                rps = input("Rock, Paper or Scissor: ")
                rps = rps.lower()
                computers = ("Rock", "Paper", "Scissors")
                computer = random.choice(computers)
                
                if ((rps == 'rock' and computer == 'Paper')or
                    (rps == 'scissors' and computer == 'Rock')or
                    (rps == 'paper' and computer == 'Scissors')):
                    print("The computer choose ", computer)
                    print(lose)
                    
                elif ((rps == 'rock' and computer == 'Scissors')
                    or (rps == 'scissors' and computer == 'Paper')
                    or (rps == 'paper' and computer == 'Rock')):
                    print("The computer choose ", computer)
                    print(win)
                    comp_lives -= 1
                    score += 1
                else:
                    print(drew)
                    draws += 1
                
                if rps == 'show rules':
                   print("""
        **********************************************
        Rules
        **********************************************
        -Rock looses against Paper
        -Rock beats Scissors
        -Paper beats Rock
        -Paper looses against Scissors
        -Scissors beats Paper
        -Scissors looses against Rock.
        **********************************************
                        """)
                if rps == 'show score':
                    print("The score is: ", score)
                if rps == 'show lives':
                    print("You have ",lives, "lives left")
                if rps == 'show computer lives':
                    print("The computer has ",comp_lives, 'lives left')
                if rps == 'show draws':
                    print("There are ",draws, "Draws")
                if rps == 'exit':
                    print("We are exiting now")
                    sys.exit()
                if lives == 0:
                    print("""
            Oh NO!
            You have lost
            Better luck next time...""")
                if comp_lives == 0:
                    print("""
            Wow!
            You have Won""")
                if rps not in words:
                    print("This wws not expected from you...so we are exiting...")
                    sys.exit()
        if password or user != password_list:
            print("Please try again")
                
            
            
            
            
            
            


