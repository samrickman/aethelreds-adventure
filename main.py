
from time import sleep
import json
import colorama
import os
from imgviewer import show_image

with open("rooms/intro.json", "r") as f:
    intro = json.load(f)

def print_preamble(room, color = colorama.Fore.CYAN):
    print(color + room['preamble'])
    print(colorama.Style.RESET_ALL)

def print_question(room, color = colorama.Fore.LIGHTBLUE_EX):
    print(color + room['question'])
    print(colorama.Style.RESET_ALL)
    image = room.get("image", None)
    if image:
        show_image(f"img/{image}")

def delay(room):
    delay = room.get('delay', 0)
    sleep(delay)    

def print_choices(room):

    choices_dict = {} # keys, 1,2,3. values, choice1, choice2, choice3
    for i, choice in enumerate(room['choices'], 1):
        choices_dict[i] = choice
        if room['type'] == "choices":
            print(f"{i}. {choice}") # print multiple choice
    answer = input(colorama.Fore.GREEN + ">> ")
    if answer == "q":
        sure = input("Are you sure? Enter y to continue.\n>> ")
        if sure == "y":
            exit()
    return choices_dict, answer

def check_answer(room, answer, choices_dict):
    
    # If choices, check choice
    if room['type'] == "choices":
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid response")
        
        if answer in choices_dict.keys():
            answer = choices_dict[answer]

    # If text, check text            
    elif room['type'] == "text":
        answer = answer.lower()
        if answer in choices_dict.values():
            for i, choice in choices_dict.items():
                if answer == choice:
                    answer = choices_dict[i]
                    break
        else:
            outcome = "IncorrectText"
            return outcome

    else:
        print("Error - room type in json must be either choices or text.")

    outcome = room['choices'].get(answer, "AnswerNotFound")
    return outcome

def unlock_room(room, room_access_permissions):
    if room.get("correct_choice", None):
        if room.get("room_to_unlock", None):
            room_access_permissions[room['room_to_unlock']]['locked'] = False
            print(colorama.Fore.YELLOW + room_access_permissions[room['room_to_unlock']]['open_message'] + colorama.Style.RESET_ALL)
            sleep(1)

def print_wrong_answer(sleep_time_in_seconds = 3):
    print(colorama.Back.RED + "ACCESS DENIED" + colorama.Style.RESET_ALL)
    sleep(sleep_time_in_seconds)

def enter_room(room, room_access_permissions, items_collected):
    """ 
    Function that takes a room as an input
    """

    print_preamble(room)

    print_question(room)    

    delay(room)

    #colorama.deinit()    
    #colorama.reinit()

    choices_dict, answer = print_choices(room)
    
    # Look up answer
    outcome = check_answer(room, answer, choices_dict)

    if outcome == "AnswerNotFound":
        print(colorama.Back.RED + "Invalid response" + colorama.Style.RESET_ALL)
        sleep(1)
        return room # back to same room
    elif outcome == "IncorrectText":
        print_wrong_answer()
        return room # back to same room
    
    
    # If we get here we have the right answer

    # Check if right answer opens another room
    unlock_room(room, room_access_permissions)

    # Check if we have permission to enter room
    #print(outcome)
    # If room permission not listed, default is we have permission to enter
    if room_access_permissions.get(outcome, {"locked" : False}).get('locked', False):
        print(f"{room_access_permissions[outcome]['message']}")

        sleep(1)
        return room # back to same room 


    # but need to check the file exists
    room_file = f"rooms/{outcome}.json"
    if os.path.exists(room_file):
        with open(f"{room_file}", "r") as f:
            next_room = json.load(f)
            if room == next_room:
                print_wrong_answer()
        return next_room
    else:
       exit(f"Room {room_file} does not exist.")
    




def main():

    if __name__ == "__main__":

        with open("room_access_permissions.json", "r") as f:
            room_access_permissions = json.load(f)

        with open("items_collected.json", "r") as f:
            items_collected = json.load(f)  

        next_room = enter_room(intro, room_access_permissions, items_collected)
        while True:
            next_room = enter_room(next_room, room_access_permissions, items_collected)

main()