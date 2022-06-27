import random

SCORE = 0
ROUNDS = 1

def player_stats():
    print(f"SCORE: {SCORE} | ROUND: {ROUNDS}")

def game_hints(USER_GUESS, Mystery_NUM):
    
    print("Would you like purchase a hint for 5 points? [1/2]: ")
    USER_HINT = int(input())
    global SCORE, divisibility, value
    if USER_HINT == 1:
        SCORE= SCORE - 5
        if Mystery_NUM % 2 == 0:
            divisibility = "even"
        else:
            divisibility = "odd"  
        if USER_GUESS > Mystery_NUM:
            value = "smaller"
        else:
            value = "larger"
        print(f"CLUE: Mystery Number is {divisibility} and try a {value} guess")     
    else:
        player_stats()
        pass    
  
def Game_Process(): 
    global ROUNDS

    while True:
        if ROUNDS <= 10:   
            Mystery_NUM = random.randrange(10)
            print(Mystery_NUM)
            while True:
                print("------------------------")
                print("Guess the Mystery Number [1-10]: ")
                USER_GUESS = int(input())
                if USER_GUESS == Mystery_NUM:
                    print("\nGood Job! +10 points!")
                    global SCORE
                    SCORE = SCORE + 10
                    ROUNDS += 1
                    player_stats()    
                    break
                else:
                    print("Wrong! Try Again")
                    SCORE = SCORE - 2
                    game_hints(USER_GUESS, Mystery_NUM)
        else:
            print("Game Over!")
            Game()        

def Game():
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
        Game_Process()
    else:
        print("Invalid Input! [1/2]")
        Game()
    
Game()
        