import random 

attempts_list=[]

def show_score() :
    if not attempts_list:
        print("There's currently no high score , Start Playing")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")

attempts = 0
rand_number = random.randint(1 , 10)

print("Hello! , Welcome to the guessing game")
player_name = input("What's your name: ").strip()
wanna_play = input(
        f"\nHi {player_name} , Would you like to play the guessing game? \n"
        "Enter Yes to play or No to quit: "
).lower().strip()

if wanna_play == "no":
    print(f"Goodbye {player_name}")
    exit()
else:
    show_score()

while wanna_play == "yes":
    try:
        guess = int(input("Pick number between 1 and 10: ").strip())
        if guess < 1 or guess > 10 :
            raise ValueError("Please Guess Numper A Between The Given Range! [1 and 10]\n")
        
        attempts += 1

        if (guess == rand_number):
            
            print("Nice You Got It!")
            print(f"It took you {attempts} attempts!\n")

            wanna_play = input(
            f"Good job {player_name} , Would you like to play again?\n"
            "Enter Yes to play or No to quit: ").lower().strip()
            
            attempts_list.append(attempts)

            if wanna_play == "no":
                    print(f"Goodbye {player_name}")
                    
            else:
                attempts= 0
                rand_number = random.randint(1 , 10)
                show_score()
                continue
        elif(guess > rand_number):
            print("It's lower")

        elif(guess < rand_number):
            print("It's higher")

    except ValueError as err :
        print(err)