# car Engine

command = ["start", "stop", "help", "quit"]

is_started = False

print("-----------------Simple Car Engine Type 'help' to get started..------------------")
while True:
    user_input = input("> ")
    if user_input == command[0]:
        if is_started:
            print(">>>>Car Is Already Started>>>>")
        else:
            is_started = True
            print(">>>>Car Is Started>>>>")

    elif user_input == command[1]:
        if not is_started:
            print(">>>>Car Is Already Stopped>>>>")
        else:
            is_started = False
            print(">>>>Car Is Stopped>>>>")

    elif user_input == command[2]:
        print("""
<---------Type These Commands To Get Started------->

~~~~~[start] To Start the Car
~~~~~[stop] To Stopped the Car
~~~~~[help] To know about Engine
~~~~~[quit] To Terminate the Engine""")

    elif user_input == command[3]:
        break
