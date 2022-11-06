import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        elif option3 == response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("You found yourself in the middle of a small Island")
    print_pause("You saw a written note on the ground that"
                "states that you have"
                "3 tasks to accomplish before you can leave the Island.")


def want_weapon(tools):
    print_pause("There will surely be dangers on your way in this journey, ")
    response = valid_input("do you want a weapon? Enter an answer"
                           "'yes' or 'no'\n", "yes", "no", "maybe")

    if response == 'no':
        print_pause("Alright then, lets move on!")
    elif response == 'yes':
        print_pause("Oh great! you will be provided with a"
                    "weapon when needed. Move!")
        tools.append('weapon')
    else:
        print_pause("Please enter yes or no")
        want_weapon(tools)


def first_task(tools):
    print_pause("You are on a quest to get the treasured Golden Sword "
                "by moving through the left path.")
    if "Golden Sword" in tools:
        print_pause("You successfully defeated the Sword Guard "
                    "and picked up the Treasured Golden Sword, so "
                    "there is nothing more to take from here, Move!")
    else:
        print_pause("You have been accosted by the ferocious Guard whom "
                    "you must defeat first before you "
                    "can get the Golden Sword")
        weapon = random.choice(["knife", "dagger", "Gun", "Battle Axe"])
        if "weapon" in tools:
            print_pause(f"fortunately you have a {weapon} with "
                        "you to scare off the Sword Guard and"
                        " you did scare off the Sword Guard")
        else:
            print_pause("unfortunately you have no weapon with you "
                        "to scare off the Sword Guard")
            print_pause("YOU LOSE!")
            play_again()
        print_pause("You then picked up the Golden Sword ")
        tools.append("Golden Sword")
    print_pause("You have to continue to your next task.")
    task_tools(tools)


def second_task(tools):
    print_pause("You have decided to get the Magic keys "
                "by moving to the forward path.")
    print_pause("After walking a few distance, You meet the "
                "Beast Master whose job is to protect the magic keys.")
    if "Magic keys" in tools:
        print_pause("Seems you already have the Magic keys.")
        print_pause("You can go ahead to the next task.")
        task_tools(tools)
    else:
        print_pause("The Beast Master confronts you in "
                    "efforts to end your journey.")
        if "Golden Sword" in tools:
            print_pause("But he saw the Golden Sword with you and ran"
                        " away and you went ahead to pick up the Magic keys.")
            tools.append("Magic keys")
            print_pause("You have to continue to your next task.")
            task_tools(tools)
        else:
            print_pause("The Beast Master accosted you and "
                        "hit you with a its gigantic head")
            print_pause("your weapon could not do anything "
                        "or contain the Beast Master")
            print_pause("You Lose!")
            play_again()


def third_task(tools):
    print_pause("You have decided to get the magic flying Boat")
    print_pause("after walking a few distance to your right")
    print_pause("you see a gigantic Gate that needs to be opened "
                "to access the magic flying Boat")
    print_pause("you pipped through the Gate and saw some "
                "Guardian Angels of the beautiful flying Boat.")
    print_pause("Yes! that is the Boat!")
    if "Golden Sword" in tools:
        print_pause("You stretched forth the Golden "
                    "Sword to the Guardian Angels.")
        print_pause("The Angels bow to you upon seeing the Golden Sword"
                    "They then ask that you use the Magic keys "
                    "to open the gigantic Gate")
        if "Magic keys" in tools:
            print_pause("Yes! you have the Magic keys")
            print_pause("You used the Magic keys to open the Gate")
            print_pause("BOOM!!! in front of you is the flying "
                        "boat presented to you by the Angels!")
            print_pause("You jumped in and off you go! YOU WIN!!!")
            play_again()
        else:
            print_pause("The Guardian Angels turned their backs on you, "
                        "and send the Beast Grandmaster that Golden "
                        "sword cannot scare to end you.")
            print_pause("YOU LOSE!")
            play_again(tools)
    else:
        print_pause("The Guardian Angels attack you "
                    "because you have no Golden Sword")
        print_pause("You need the Golden Sword to be "
                    "acknowledged by the Guardian Angels")
        print_pause("YOU LOSE!")
        play_again()


def task_tools(tools):
    print_pause("Please enter the number for the"
                "task you would like to accomplish:")
    response = valid_input("1. Get the Treasured Golden sword\n"
                           "2. Get the Magic Keys\n"
                           "3. Get the Magic Flying Boat\n",
                           "1", "2", "3")
    if response == '1':
        first_task(tools)
    elif response == '2':
        second_task(tools)
    elif response == '3':
        third_task(tools)
    else:
        print_pause("Please enter 1 or 2 or 3")
        task_tools(tools)


def play_again():
    response = valid_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no", "maybe")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        adventure_game()
    else:
        print_pause("Please enter yes or no")
        play_again()


def adventure_game():
    tools = []
    intro()
    want_weapon(tools)
    task_tools(tools)
    play_again()


if __name__ == "__main__":
    adventure_game()
