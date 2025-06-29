import random

# 📝 قائمة لحفظ السكور لكل لاعب
high_scores = {}

def show_score(player_name):
    if player_name in high_scores:
        print(f"🏆 Your best score is {high_scores[player_name]} attempts.\n")
    else:
        print("There's currently no high score. Start playing to set one!\n")

def choose_difficulty():
    levels = {
        "easy": 5,
        "medium": 10,
        "hard": 50
    }

    while True:
        level = input("Choose difficulty (easy / medium / hard): ").lower().strip()
        if level in levels:
            print(f"🎯 You selected {level.title()} mode! Guess a number between 1 and {levels[level]}.\n")
            return levels[level]
        else:
            print("Please enter a valid difficulty level (easy / medium / hard).")

def get_player_name():
    print("🎮 Hello! Welcome to the guessing game.")
    return input("What's your name? ").strip()

def ask_to_play(player_name):
    return input(
        f"\nHi {player_name}, would you like to play the guessing game?\n"
        "Enter yes to play or no to quit: "
    ).lower().strip()

def play_game(player_name, max_number, round_number):
    rand_number = random.randint(1, max_number)
    attempts = 0

    print(f"🎲 Round {round_number} begins!")
    
    while True:
        try:
            guess = int(input(f"Pick a number between 1 and {max_number}: ").strip())

            if guess < 1 or guess > max_number:
                raise ValueError(f"⚠️ Please guess a number between 1 and {max_number}.")

            attempts += 1

            if guess == rand_number:
                print(f"\n🎉 Nice! You got it in {attempts} attempts.")

                if attempts == 1:
                    print("😲 Wow, you're a genius!\n")
                elif attempts <= 3:
                    print("💪 Great job!\n")
                else:
                    print("✅ Well done!\n")

                # 🏅 تحديث أفضل سكور
                if player_name not in high_scores or attempts < high_scores[player_name]:
                    high_scores[player_name] = attempts

                break

            elif guess > rand_number:
                print("🔻 It's lower.")
            else:
                print("🔺 It's higher.")

        except ValueError as err:
            print(err)

def main():
    player_name = get_player_name()
    round_number = 1

    while True:
        wanna_play = ask_to_play(player_name)
        
        while wanna_play not in ["yes", "no"]:
            wanna_play = input("Please enter yes or no: ").lower().strip()

        if wanna_play == "no":
            print(f"👋 Goodbye, {player_name}!")
            break

        show_score(player_name)
        max_number = choose_difficulty()
        play_game(player_name, max_number, round_number)
        round_number += 1

# 🚀 Run the game
if __name__ == "__main__":
    main()
