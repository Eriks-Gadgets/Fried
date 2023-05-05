#Fried
#(c) 2023 Erik's Gadgets

import PySimpleGUI as sg #Imports GUI Library
import os 

cutscene1_stage = 0

login = os.getlogin()

import random

sg.theme("DarkTeal12") #Sets theme

sg.Popup("Fried\n(c) 2023 Erik's Gadgets") #IP addition

room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room.png")], [sg.Button("Start Tutorial"), sg.Button("Continue")]])

while True:
    event, values = room.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Start Tutorial":
        room.close()
        cutscene1_stage = 1
        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room.png")], [sg.Text("Welcome to YOUR brand new resturaunt\nThis is the kitchen!"), sg.Button("Continue")]])
    if event == "Continue":
        if cutscene1_stage == 1:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room.png")], [sg.Text("Let's buy a Fridge so that we have something to prevent the food from, well\nexpiring."), sg.Button("Continue")]])
            cutscene1_stage += 1
        elif cutscene1_stage == 2:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room1.png")], [sg.Text("No one likes ugly, raw meat\n(including the fact that it gives you food poisoning)\nLet's buy a grill so that we can cook the meat!\n..and also to prevent Food Poisoning."), sg.Button("Continue")]])
            cutscene1_stage += 1
        elif cutscene1_stage == 3:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room2.png")], [sg.Text("Alright! Let's Begin Cooking!!"), sg.Button("Continue")]])
            cutscene1_stage = 0
        elif cutscene1_stage == 0:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room2.png")], [sg.Button("Fridge"),sg.Button("Grill")]])
            hasHotDogs = False
            hotDogsState = "Raw"
            ketchup = False
            orders = ["Hot Dog, Plain", "Hot Dog, with Ketchup"]
            random_num = random.randint(0,len(orders) - 1)
            sg.Popup(orders[random_num])
            if random_num == 0:
                ketchupRequired = False
            elif random_num == 1:
                ketchupRequired = True
            cutscene1_stage = -1
        elif cutscene1_stage == -1:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room2.png")], [sg.Button("Fridge"),sg.Button("Grill")]])
        elif cutscene1_stage == -2:
            cutscene1_stage = -5
            if hotDogsState == "Raw":
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-raw.png")], [sg.Button("Dress with Ketchup"),sg.Button("Continue")]])
            elif hotDogsState == "Cooked":
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked.png")], [sg.Button("Dress with Ketchup"),sg.Button("Continue")]])
            elif hotDogsState == "Burnt":
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt.png")], [sg.Button("Dress with Ketchup"),sg.Button("Continue")]])
        elif cutscene1_stage == -3:
            room.close()
            cutscene1_stage = -4
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt-to-a-crisp.png")], [sg.Text("OH NO! You've burnt the hot dog! It's now a pile of ashes...")], [sg.Button("Continue")]])
        elif cutscene1_stage == -4:
            room.close()
            cutscene1_stage = -1
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-crisp.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")]])
        elif cutscene1_stage == -5:
            ketchup_style = 0
            if hotDogsState == "Raw":
                room.close()
                cutscene1_stage = -7
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-raw-1.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
            if hotDogsState == "Cooked":
                room.close()
                cutscene1_stage = -7
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-cooked-1.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
            if hotDogsState == "Burnt":
                room.close()
                cutscene1_stage = -7
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-burnt-1.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
        elif cutscene1_stage == -6:
            if ketchup_style == 1:
                if hotDogsState == "Raw":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-raw-2.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-cooked-2.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-burnt-2.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
            elif ketchup_style == 1:
                if hotDogsState == "Raw":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-raw-3.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-cooked-3.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-burnt-3.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
        elif cutscene1_stage == -8:
            cutscene1_stage = 0
            if ketchupRequired == False:
                if hotDogsState == "Burnt":
                    if ketchup_style != 0:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-no-topping-burnt.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")]])
                    if ketchup_style == 0:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-burnt-with-toppings.png")], [sg.Text("Well, It's not BAD... It's not good either but it's not bad.")],[sg.Button("Continue")]])    
                if hotDogsState == "Cooked":
                    if ketchup_style != 0:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-bad-presentation.png")], [sg.Text("4 Stars! Pretty Good.")],[sg.Button("Continue")]])  
                    if ketchup_style == 0:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-amazing-presentation.png")], [sg.Text("Great Job! All Five Stars!")],[sg.Button("Continue")]])  
                if hotDogsState == "Raw":
                    if ketchup_style != 0:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")]])
                    if ketchup_style == 0:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw-with-toppings.png")], [sg.Text("Two Stars are better than None... I guess...")],[sg.Button("Continue")]])
            if ketchupRequired == True and ketchup_style == 0:
                if hotDogsState == "Burnt":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-no-topping-burnt.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-no-topping-cooked.png")], [sg.Text("Two Stars are better than None... I guess...")],[sg.Button("Continue")]])
                if hotDogsState == "Raw":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")]])
            if ketchupRequired == True and ketchup_style != 0 and hotDogsState == "Cooked":
                if ketchup_style == 2:
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-amazing-presentation.png")], [sg.Text("Great Job! All Five Stars!")],[sg.Button("Continue")]])    
                if ketchup_style == 1:
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-bad-presentation.png")], [sg.Text("4 Stars! Pretty Good.")],[sg.Button("Continue")]])    
            if ketchupRequired == True and ketchup_style != 0 and hotDogsState != "Cooked":
                if hotDogsState == "Burnt":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-burnt-with-toppings.png")], [sg.Text("Well, It's not BAD... It's not good either but it's not bad.")],[sg.Button("Continue")]])    
                if hotDogsState == "Raw":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw-with-toppings.png")], [sg.Text("Two Stars are better than None... I guess...")],[sg.Button("Continue")]])    
        elif cutscene1_stage == -7:
            if ketchup_style == 0:
                if hotDogsState == "Raw":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-raw-1.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-cooked-1.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-burnt-1.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
            elif ketchup_style == 1:
                if hotDogsState == "Raw":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-raw-2.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-cooked-2.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-burnt-2.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
            elif ketchup_style == 2:
                if hotDogsState == "Raw":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-raw-3.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-cooked-3.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    cutscene1_stage = -8
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-burnt-3.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])        
    if event == "Grill":
        if hasHotDogs == False:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room4.png")], [sg.Text("It appears you don't have anything to 'Grill' just yet."), sg.Button("Continue")]])
        elif hasHotDogs == True:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room4.png")], [sg.Text("Cook the Hot Dogs for "), sg.Input(), sg.Text(" Minutes."), sg.Button("Cook")]])
    if event == "Dress with Ketchup":
        cutscene1_stage = -6
        random_num = random.randint(1, 2)
        if random_num == 1:
            if hotDogsState == "Raw":
                room.close()
                ketchup_style = 1
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-raw-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
            if hotDogsState == "Cooked":
                room.close()
                ketchup_style = 1
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
            if hotDogsState == "Burnt":
                room.close()
                ketchup_style = 1
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
        else:
            if hotDogsState == "Raw":
                room.close()
                ketchup_style = 2
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-raw-ketchup2.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
            if hotDogsState == "Cooked":
                room.close()
                ketchup_style = 2
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
            if hotDogsState == "Burnt":
                room.close()
                ketchup_style = 2
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
    if event == "Cook":
        if int(values[1]) < 10 and int(values[1]) > 0:
            hotDogsState = "Raw"
            hasHotDogs = 0
            room.close()
            cutscene1_stage = -2
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-raw.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
        elif int(values[1]) < 13 and int(values[1]) > 0:
            hotDogsState = "Cooked"
            hasHotDogs = 0
            room.close()
            cutscene1_stage = -2
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-cooked.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
        elif int(values[1]) < 30 and int(values[1]) > 0:
            hotDogsState = "Burnt"
            hasHotDogs = 0
            room.close()
            cutscene1_stage = -2
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-burnt.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
        else:
            crisp = True
            hotDogsState = "Burnt"
            hasHotDogs = 0
            room.close()
            cutscene1_stage = -3
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-burnt.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
    if event == "Fridge":
        if hasHotDogs == False:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room3.png")], [sg.Text("Let's Grab some Hot Dogs."), sg.Button("Continue")]])
            hasHotDogs = True
        elif hasHotDogs == True:
            room.close()
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room3_no_hotdogs.png")], [sg.Text("We ran out hotdogs!"), sg.Button("Continue")]])
            hasHotDogs = True
room.close()
