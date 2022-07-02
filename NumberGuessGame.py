import random

def player_stats():
    print(f"{player_name}: POINTS: {points} | ROUND: {rounds}")

def game_hints():
    global points
    user_hint = input("Would you like purchase a hint for 5 points? [Y/N]: ").lower()
    print("\n")
    if user_hint == "y":
        points -= 5
        if Mystery_NUM % 2 == 0:
            divisibility = "even"
        else:
            divisibility = "odd"    
        if player_guess > Mystery_NUM:
            value = "smaller"
        else:
            value = "larger"  
        print(f"CLUE: Mystery Number is {divisibility} and try a {value} guess | -5 POINTS")
    elif user_hint == "n":  
        player_stats()
        pass   
    else:
        print("Invalid Input!")
        game_hints()
        
def scoreboard_sort(line):
    player_data = line.split('|')
    player_score = int(player_data[-1])
    return player_score      
    
def game_scoreboard():
    Scoreboard_add = open("SCOREBOARD.txt", "a")
    Scoreboard_add.write(f"{player_name} | {points}")
    Scoreboard_add.write("\n")
    Scoreboard_add.close()
    
    
    Scoreboard_view = open("SCOREBOARD.txt", 'r')
    Scoreboard = Scoreboard_view.readlines()
    Scoreboard.sort(key=scoreboard_sort, reverse=True)
    for player_data in Scoreboard:
        print(player_data)
        
    Scoreboard_view.close()


  
def Game_Process(): 
    global points, rounds, Mystery_NUM, player_guess
    points = 0
    rounds = 0
    while True:  
        if rounds <= 10:   
            Mystery_NUM = random.randrange(10)
            print(Mystery_NUM) #remove this after final product
            while True:
                print("------------------------")
                player_guess = int(input("Guess the Mystery Number [1-10]: "))
                if player_guess == Mystery_NUM:
                    print("\nGood Job! +10 points!")
                    points = points + 10
                    rounds += 1
                    player_stats()    
                    break
                else:
                    print("Wrong! Try Again | -2 POINTS")
                    points -= 2
                    game_hints()
        else:
            print("Game Over!")
            print("\n")
            print("SCOREBOARD: ")
            print("\n")
            game_scoreboard()
            Main()        

def Main():
    global player_name
    user_opt = input("\"Welcome to Guess Game\" \nPress [Y] to Play or [N] to Exit: ").lower()
    if user_opt == "n":
        print("Good bye!")
        exit()
    elif user_opt == "y":
        print("""\nMechanics: 
            1. Correct Guess: +10 points 
            2. Incorrent Guess: -2
            3. Clue cost: 5 points
            4. 10 rounds per game.""")
        player_name = input("Enter name: ")
        if player_name == "":
            print("Kindly enter a valid name")  
            Main()   
        else:
            Game_Process()       
    else:
        print("Invalid Input!")
        Main()
    
Main()
        