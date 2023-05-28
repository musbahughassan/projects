import random # we need to use random module to allow computer to make choice

option = ["r", "p", "s"]
user_wins = 0
ai_wins = 0

print("Type 'y' to play or 'q' to quit. ")

while True:
    user_input = input("r / p / s: ")
    if user_input == "q":
        break
    elif user_input not in option:
        continue

    ai_pick = random.choice(option)
    print(f"A.I picked {ai_pick.upper()} and You picked {user_input.upper()}")
    if user_input == ai_pick:
        user_wins += 1
        print("You Win")
        
    elif user_input != ai_pick:
        ai_wins += 1
        print("A.I Win")
print("-------You scored: ", user_wins)
print("-------A.I scored: ", ai_wins)
if ai_wins > user_wins:
    print("--------You are Eliminated.-------")
    print("------------TryAgain--------------")
elif user_wins > ai_wins:
    print("--------You Won The Match.-------")
    print("--------You are The Champion-----")
